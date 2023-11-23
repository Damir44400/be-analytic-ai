from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.genre_schema import GenreCreate
from . import router, genre_repo


@router.patch("/genres/{genre_id}")
async def update_producers(genre_id: int, genre: GenreCreate, db: Session = Depends(get_db),
                           user: UserOut = Depends(get_current_user)):
    if user.is_moderator or user.is_superuser:
        db_genre = genre_repo.get_genre_by_id(db, genre_id)
        if db_genre:
            genre_repo.update_producer(db, genre_id, genre)
            return {"message": f"{db_genre.name} successful updated"}
        return HTTPException(detail="The producer not found", status_code=status.HTTP_404_NOT_FOUND)
    return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
