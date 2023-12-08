from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from app.schemas.anime_schema import Anime
from . import (router, genre_anime_repo,
               anime_repo,
               category_repo)


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

            anime = {
                "id": db_anime.id,
                "title": db_anime.title,
                "cover": db_anime.cover,
                "category": category_name,
                "description": db_anime.description[:50],
                "date_uploaded": db_anime.date_uploaded
            }
            animes.append(anime)
        return animes
    return []
