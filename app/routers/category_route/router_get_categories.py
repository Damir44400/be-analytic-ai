from fastapi import Depends
from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, category_repo


@router.get("/categories")
async def all_categories(db: Session = Depends(get_db)):
    return category_repo.get_all_categories(db)
