from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.studio_schema import StudioCreate
from . import router, studio_repo


@router.post("/studios")
async def post_studios(studio: StudioCreate, db: Session = Depends(get_db),
                       user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            if studio_repo.get_studio_by_name(db, studio.name):
                raise HTTPException(detail="The studio already exists", status_code=status.HTTP_409_CONFLICT)
            studio_repo.create_studio(db, studio)
            return {"message": f"{studio.name} successful created"}
        raise HTTPException(detail="Only superuser or moderator has access", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail=e.__class__.__name__, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
