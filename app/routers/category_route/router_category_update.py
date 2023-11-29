from datetime import date

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.category_schema import CategoryBase
from . import router, category_repo


@router.patch("/categories/{category_id}")
async def update_categories(category_id: int, new_category: CategoryBase, db: Session = Depends(get_db),
                            user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            db_category = category_repo.get_anime_date_by_id(db, category_id)
            if db_category:
                category_repo.update_category(db, category_id, new_category.name)
                return {"message": f"{db_category.name} successful updated to {new_category.name}"}
            return HTTPException(detail="The category not found", status_code=status.HTTP_404_NOT_FOUND)
        return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail=e.__class__.__name__ + "Internal Server Error",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
