from . import router,user_schema
from fastapi import Depends

from app.depends import get_current_user


@router.get('/profile', summary='Get details of currently logged in user', response_model=user_schema.UserProfile)
async def get_me(user: user_schema.UserProfile = Depends(get_current_user)):
    return user
