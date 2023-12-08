from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db
from app.schemas.anime_schema import Anime
from . import (router, genre_anime_repo,
               anime_repo,
               genre_repo,
               category_repo,
               studio_repo,
               producer_repo,
               rating_repo,
               comment_repo,
               user_repo)


@router.get("/animes/{anime_id}")
async def anime_chapter(anime_id: int, db: Session = Depends(get_db)):
    try:
        db_anime = anime_repo.get_anime_by_id(db, anime_id)
        if db_anime:
            db_category = category_repo.get_category_by_id(db, db_anime.category_id)
            db_studio = studio_repo.get_studio_by_id(db, db_anime.studio_id)
            studio_id = None
            studio_name = ""
            if db_studio:
                studio_id = db_studio.id
                studio_name = db_studio.name

            producer_name = ""
            producer_id = None
            db_producer = producer_repo.get_producer_by_id(db, db_anime.producer_id)
            if db_producer:
                producer_id = db_producer.id
                producer_name = db_producer.name

            anime_genres = [genre.genre_id for genre in genre_anime_repo.get_genre_anime_by_anime_id(db, anime_id)]
            anime = Anime(
                id=db_anime.id,
                title=db_anime.title,
                description=db_anime.description,
                cover=db_anime.cover,
                date_announced=db_anime.date_announced,
                country=db_anime.country,
                genres=genre_repo.get_genres_by_ids(db, list(anime_genres)),
                category={"category_id": db_category.id, "category_name": db_category.name},
                studio={"studio_id": studio_id, "studio_name": studio_name},
                producer={"producer_id": producer_id, "producer_name": producer_name}).dict()

            rating_of_anime = rating_repo.get_rating_anime(db, anime_id)
            ratings = [{"stars": db_rating.stars} for db_rating in rating_of_anime]
            total_rating = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
            for rating in ratings:
                for k, v in rating.items():
                    total_rating[v] += 1

            average_rating = sum(rating['stars'] for rating in ratings) / len(ratings) if ratings else 0

            anime["rating"] = {"average": average_rating, "individual": total_rating}

            db_comments = comment_repo.get_comment_of_anime(db, anime_id)
            comments = []
            for comment in db_comments:
                tmp_comment = {
                    "user": {
                        "id": comment.user_id,
                        "username": user_repo.get_user_by_id(db, comment.user_id).username
                    },
                    "content": comment_repo.get_comment_by_id(db, comment.id).content,
                    "date_upload": comment_repo.get_comment_by_id(db, comment.id).date_uploaded
                }
                comments.append(tmp_comment)
            anime["comments"] = comments
            return anime
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The title not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
