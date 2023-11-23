from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, producer_repo


@router.get("/producers")
async def all_producers(db: Session = Depends(get_db)):
    return producer_repo.get_all_producers(db)
