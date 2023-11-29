from . import router, rating_repo, anime_repo
from app.depends import get_db

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status


@router.get("/rating/{anime_id}")
def get_anime_rating(anime_id: int, db: Session = Depends(get_db)):
    try:
        if anime_repo.get_anime_by_id(db, anime_id):
            total_stars = rating_repo.get_rating_anime(db, anime_id)
            return total_stars
        raise HTTPException(detail="The anime not found", status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
