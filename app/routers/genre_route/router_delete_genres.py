from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from . import router, genre_repo


@router.delete("/genres/{genre_id}")
async def delete_producers(genre_id: int, db: Session = Depends(get_db),
                           user: UserOut = Depends(get_current_user)):
    if user.is_moderator or user.is_superuser:
        db_genre = genre_repo.get_genre_by_id(db, genre_id)
        if db_genre:
            genre_repo.delete_genre(db, genre_id)
            return {"message": f"{db_genre.name} successful deleted"}
        return HTTPException(detail="The genre not found", status_code=status.HTTP_404_NOT_FOUND)
    return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
