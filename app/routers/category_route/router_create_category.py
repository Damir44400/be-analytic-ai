from . import router, category_repo
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.category_schema import CategoryCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status


@router.post("/categories")
def create_categories(category: CategoryCreate, db: Session = Depends(get_db),
                      user: UserOut = Depends(get_current_user)):
    try:
        if user.is_moderator or user.is_superuser:
            if category_repo.get_category_by_name(db, category.name):
                raise HTTPException(detail="The category already exists", status_code=status.HTTP_409_CONFLICT)
            category_repo.create_category(db, category.name)
            return {"message": f"{category.name} successful created"}
        return HTTPException(detail="Only superuser or moderator has access", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail=e.__class__.__name__, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
