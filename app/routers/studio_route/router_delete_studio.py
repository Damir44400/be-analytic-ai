from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from . import router, studio_repo


@router.delete("/studios/{studio_id}")
async def delete_studios(studio_id: int, db: Session = Depends(get_db),
                         user: UserOut = Depends(get_current_user)):
    if user.is_moderator or user.is_superuser:
        db_studio = studio_repo.get_studio_by_id(db, studio_id)
        if db_studio:
            studio_repo.delete_studio(db, studio_id)
            return {"message": f"{db_studio.name} successful deleted"}
        return HTTPException(detail="The producer not found", status_code=status.HTTP_404_NOT_FOUND)
    return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
