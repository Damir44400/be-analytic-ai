from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from . import router, announce_repo


@router.delete("/release-dates/{date_id}")
async def delete_date(date_id: int, db: Session = Depends(get_db),
                      user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            db_date = announce_repo.get_anime_date_by_id(db, date_id)
            if db_date:
                announce_repo.delete_anime_date(db, date_id)
                return {"message": f"{db_date.year} successful deleted"}
            return HTTPException(detail="The year not found", status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(detail="Only superuser or moderator has access", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
