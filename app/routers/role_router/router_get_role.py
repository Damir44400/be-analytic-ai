from sqlalchemy.orm import Session

from . import router, user_repo
from app.depends import get_current_user, get_db
from fastapi import Depends, HTTPException, status
from app.schemas.user_schema import UserOut


@router.get("/moderators")
def get_moderators(db: Session = Depends(get_db), user: UserOut = Depends(get_current_user)):
    if user.is_superuser:
        return user_repo.get_moderators(db)
    return HTTPException(detail="Not access to data", status_code=status.HTTP_403_FORBIDDEN)


@router.get("/users")
def get_users(db: Session = Depends(get_db), user: UserOut = Depends(get_current_user)):
    if user.is_superuser:
        return user_repo.get_all(db)
    return HTTPException(detail="Not access to data", status_code=status.HTTP_403_FORBIDDEN)
