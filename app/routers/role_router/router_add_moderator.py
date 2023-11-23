from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserOut
from . import router, role_repo, user_repo
from app.depends import get_current_user, get_db


@router.post("/moderators/{user_id}")
async def delete_moderator(user_id: int, user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.is_superuser:
        user_db = user_repo.get_user_by_id(db, user_id)
        if not user_db:
            raise HTTPException(detail="The user not found", status_code=status.HTTP_404_NOT_FOUND)
        if user_db.role_id in (3, 1):
            role_repo.add_moderator(user_id)
            return {"message": "The user was moderator"}
        else:
            raise HTTPException(detail="The user already moderator", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        raise HTTPException(detail="Forbidden", status_code=status.HTTP_403_FORBIDDEN)
