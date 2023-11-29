from aioredis import Redis
from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from app.schemas.anime_schema import Anime
from . import router, genre_anime_repo, anime_repo, genre_repo, category_repo, studio_repo, producer_repo


@router.get("/animes")
async def all_animes(db: Session = Depends(get_db)):
    db_animes = genre_anime_repo.get_all_genre_animes(db)
    if db_animes:
        animes_dict = {anime.anime_id: set() for anime in db_animes}
        for anime in db_animes:
            animes_dict[anime.anime_id].add(anime.genre_id)

        animes = []
        for anime_id, genre_ids in animes_dict.items():
            db_anime = anime_repo.get_anime_by_id(db, anime_id)
            category_name = category_repo.get_category_by_id(db,
                                                             db_anime.category_id).name if db_anime.category_id else None
            studio_name = studio_repo.get_studio_by_id(db, db_anime.studio_id).name if db_anime.studio_id else None
            producer_name = producer_repo.get_producer_by_id(db,
                                                             db_anime.producer_id).name if db_anime.producer_id else None

            anime = Anime(
                id=db_anime.id,
                title=db_anime.title,
                description=db_anime.description,
                cover=db_anime.cover,
                date_announce=db_anime.date_announce,
                country=db_anime.country,
                genres=genre_repo.get_genres_by_ids(db, list(genre_ids)),
                category=category_name,
                studio=studio_name,
                producer=producer_name,
                date_uploaded=db_anime.date_uploaded,
                date_updated=db_anime.date_updated
            )
            animes.append(anime)
        return animes
    return []
