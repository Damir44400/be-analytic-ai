from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, genre_anime_repo, anime_repo, category_repo, genre_repo


@router.get("/genres/{genre_id}/animes")
async def all_animes_genre(genre_id: int, db: Session = Depends(get_db)):
    db_animes = genre_anime_repo.get_animes_by_genre(db, genre_id)
    genre_name = genre_repo.get_genre_by_id(db, db_animes[0].genre_id).name
    animes = []
    for anime in db_animes:
        db_anime = anime_repo.get_anime_by_id(db, anime.anime_id)
        category_name = category_repo.get_category_by_id(db,
                                                         db_anime.category_id).name if db_anime.category_id else None
        anime = {
            "id": db_anime.id,
            "title": db_anime.title,
            "cover": db_anime.cover,
            "category": category_name,
            "description": db_anime.description[:50],
            "date_uploaded": db_anime.date_uploaded
        }
        animes.append(anime)
    return {"genre": genre_name, "animes": animes}
