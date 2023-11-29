from datetime import date
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.date_announce_schema import AnnounceSchemaBase
from . import router, announce_repo


@router.patch("/release-dates/{date_id}")
async def update_date(date_id: int, new_date: AnnounceSchemaBase, db: Session = Depends(get_db),
                      user: UserOut = Depends(get_current_user)):
    try:
        if not (user.is_moderator or user.is_superuser):
            raise HTTPException(detail="You are not a superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
        db_date = announce_repo.get_anime_date_by_id(db, date_id)
        if not db_date:
            raise HTTPException(detail="The year not found", status_code=status.HTTP_404_NOT_FOUND)
        new_date_obj = date(year=new_date.year, month=1, day=1)
        announce_repo.update_anime_date(db, date_id, new_date.year)
        return {"message": f"{db_date.year} successfully updated to {new_date.year}"}
    except Exception as e:
        raise HTTPException(detail=f"{e.__class__.__name__}: Internal Server Error",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
