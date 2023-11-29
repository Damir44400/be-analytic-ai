from datetime import date

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.date_announce_schema import AnnounceSchemaBase
from . import router, announce_repo


@router.post("/release-dates")
async def post_date(announce_year: AnnounceSchemaBase, db: Session = Depends(get_db),
                    user: UserOut = Depends(get_current_user)):
    try:
        if not (user.is_moderator or user.is_superuser):
            raise HTTPException(
                detail="Only superuser or moderator has access",
                status_code=status.HTTP_403_FORBIDDEN
            )

        corr_date = date(year=announce_year.year, month=1, day=1)

        if announce_repo.get_anime_date_by_release_date(db, release_date=announce_year.year):
            raise HTTPException(
                detail="The year already exists",
                status_code=status.HTTP_409_CONFLICT
            )

        announce_repo.create_anime_date(db, announce_year.year)
        return {"message": f"{announce_year.year} successfully created"}

    except IntegrityError as e:
        db.rollback()
        return HTTPException(
            detail=f"IntegrityError: {e}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
