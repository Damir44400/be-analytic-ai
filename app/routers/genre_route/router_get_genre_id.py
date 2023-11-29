from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, genre_anime_repo


@router.get("/genres/{genre_id}")
async def all_animes_genre(genre_id: int, db: Session = Depends(get_db)):
    animes = genre_anime_repo.get_animes_by_genre(db, genre_id)
    print(list(animes))
    return animes
