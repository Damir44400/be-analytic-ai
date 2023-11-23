from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, anime_repo


@router.get("/genres/{genre_id}")
async def all_animes_genre(genre_id: int, db: Session = Depends(get_db)):
    animes = [anime for anime in anime_repo.get_all_anime(db) if anime.genre.id == genre_id]
    return animes
