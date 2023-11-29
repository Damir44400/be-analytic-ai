from . import router, rating_repo
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


@router.delete("/rating/{anime_id}")
def delete_rating(anime_id: int, db: Session = Depends(get_db), user: UserOut = Depends(get_current_user)):
    try:
        deleted = rating_repo.delete_rating(db, anime_id, user.id)
        if deleted:
            return {"message": "Rating deleted successfully"}
        else:
            raise HTTPException(detail="Rating not found", status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
