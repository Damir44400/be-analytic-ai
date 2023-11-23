from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, genre_repo


@router.get("/genres")
async def all_genres(db: Session = Depends(get_db)):
    return genre_repo.get_all_genres(db)
