from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, category_repo


@router.get("/categories/{category_id}")
async def category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = category_repo.get_category_by_id(db, category_id)
