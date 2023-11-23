from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.genre_schema import GenreCreate
from . import router, genre_repo


@router.post("/genres")
async def post_genre(genre: GenreCreate, db: Session = Depends(get_db),
                     user: UserOut = Depends(get_current_user)):
    if user.is_moderator or user.is_superuser:
        genre_repo.create_genre(db, genre.name)
        return {"message": f"{genre.name} successful created"}
    return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
