from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from . import router, category_repo


@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, db: Session = Depends(get_db),
                          user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            db_category = category_repo.get_category_by_id(db, category_id)
            if db_category:
                category_repo.delete_category(db, category_id)
                return {"message": f"{db_category.name} successful deleted"}
            return HTTPException(detail="The category not found", status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(detail="Only superuser or moderator has access", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail=e.__class__.__name__, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
