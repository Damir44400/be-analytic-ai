from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, announce_repo


@router.get("/release-dates")
async def all_dates(db: Session = Depends(get_db)):
    return announce_repo.get_all_announce_dates(db)
