from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.studio_schema import StudioUpdate
from . import router, studio_repo


@router.patch("/studios/{studio_id}")
async def update_producers(studio_id: int, studio: StudioUpdate, db: Session = Depends(get_db),
                           user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            db_studio = studio_repo.get_studio_by_id(db, studio_id)
            if db_studio:
                studio_repo.update_studio(db, studio_id, studio)
                return {"message": f"{db_studio.name} successful updated to {studio.name}"}
            return HTTPException(detail="The producer not found", status_code=status.HTTP_404_NOT_FOUND)
        return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail=e.__class__.__name__ + "Internal Server Error",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
