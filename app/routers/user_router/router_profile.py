from sqlalchemy.orm import Session

from . import router, user_repo, comment_repo
from fastapi import Depends

from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserProfile, UserOut


@router.get('/profile', summary='Get details of currently logged in user', response_model=UserProfile)
async def profile(user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    user_profile = user_repo.get_user_by_id(db, user_id=user.id)
    total_comment = len(comment_repo.get_comments_by_user_id(db, user.id))
    return UserProfile(
        id=user_profile.id,
        email=user_profile.email,
        username=user_profile.username,
        profile_photo=user_profile.profile_photo,
        registered_at=user_profile.registered_at,
        comments=total_comment,
        is_superuser=user.is_superuser,
        is_moderator=user.is_moderator
    )
