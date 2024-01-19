from . import router, comment_repo, user_repo
from app.depends import get_db
from app.schemas.user_schema import UserGet
from sqlalchemy.orm import Session
from fastapi import Depends


@router.get("/users/get-user/{user_id}")
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    db_user = user_repo.get_user_by_id(db, user_id)
    total_comment = len(comment_repo.get_comments_by_user_id(db, user_id))
    return UserGet(username=db_user.username, profile_photo=db_user.profile_photo, comments=total_comment)
