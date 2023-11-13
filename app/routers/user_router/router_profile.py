from sqlalchemy.orm import Session

from . import router, user_repo
from fastapi import Depends

from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserProfile, UserOut


@router.get('/profile', summary='Get details of currently logged in user', response_model=UserProfile)
async def profile(user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    user_profile = user_repo.get_user_by_id(db, user_id=user.id)
    return UserProfile(
        id=user_profile.id,
        username=user_profile.username,
        profile_photo=user_profile.profile_photo,
        registered_at=user_profile.registered_at,
        is_active=True
    )
