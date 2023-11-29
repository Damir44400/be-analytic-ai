from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, studio_repo


@router.get("/studios")
async def all_studios(db: Session = Depends(get_db)):
    return studio_repo.get_all_studios(db)
