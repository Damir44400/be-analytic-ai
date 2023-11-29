from . import router, anime_repo
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut

from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from .utilits import check_user_privileges


@router.delete("/animes/{anime_id}")
async def delete_anime(anime_id: int, db: Session = Depends(get_db), user: UserOut = Depends(get_current_user)):
    try:
        check_user_privileges(user)
        anime_db = anime_repo.get_anime_by_id(db, anime_id)
        if anime_db:
            anime_repo.delete_anime(db, anime_id)
            return {"message": f"The title {anime_db.title} successful deleted"}
        else:
            raise HTTPException(detail="The title not found", status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
