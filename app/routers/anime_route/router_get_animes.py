from fastapi import Depends, Query
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, genre_anime_repo, anime_repo, genre_repo


@router.get("/animes")
async def all_genres(skip=Query(None), limit=Query(None), db: Session = Depends(get_db)):
    animes = genre_anime_repo.get_genre_animes(db)
    all_animes = []
    for anime in animes:
        db_anime = anime_repo.get_anime_by_id(db, anime.anime_id)
        all_animes.append(db_anime)
    print(all_animes)
