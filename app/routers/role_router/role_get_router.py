from sqlalchemy.orm import Session

from . import router, role_repo, user_repo
from app.depends import get_current_user, get_db
from fastapi import Depends, HTTPException, status
from app.schemas.user_schema import UserOut


@router.post("/moderators")
def get_moderators(user: UserOut = Depends(get_current_user)):
    if user.is_superuser:
        return role_repo.get_all_moderators()
    return HTTPException(detail="Not access to data", status_code=status.HTTP_403_FORBIDDEN)


@router.post("/users")
def get_users(db: Session = Depends(get_db), user: UserOut = Depends(get_current_user)):
    if user.is_superuser:
        return user_repo.get_all(db)
    return HTTPException(detail="Not access to data", status_code=status.HTTP_403_FORBIDDEN)
