from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.genre_schema import GenreCreate
from . import router, genre_repo


@router.post("/genres")
async def post_genre(genre: GenreCreate, db: Session = Depends(get_db),
                     user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            if genre_repo.get_genre_by_name(db, genre.name):
                raise HTTPException(detail="The genre already exists", status_code=status.HTTP_409_CONFLICT)
            genre_repo.create_genre(db, genre.name)
            return {"message": f"{genre.name} successful created"}
        raise HTTPException(detail="Only superuser or moderator has access", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail=e.__class__.__name__, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
