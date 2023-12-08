from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.genre_schema import GenreCreate
from . import router, genre_repo


@router.patch("/genres/{genre_id}")
async def update_genre(genre_id: int, genre: GenreCreate, db: Session = Depends(get_db),
                       user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            db_genre = genre_repo.get_genre_by_id(db, genre_id)
            prev_name = db_genre.name
            if db_genre:
                genre_repo.update_genre(db, genre_id, genre.name)
                return {"message": f"{prev_name} successful updated to {genre.name}"}
            return HTTPException(detail="The genre not found", status_code=status.HTTP_404_NOT_FOUND)
        return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        print(e)
        raise HTTPException(detail=e.__class__.__name__ + " Internal Server Error",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
