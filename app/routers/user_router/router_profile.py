from sqlalchemy.orm import Session

from . import router, user_repo
from fastapi import Depends

from app.depends import get_current_user, get_db
from ...schemas.user_schema import User


@router.get('/profile', summary='Get details of currently logged in user')
async def profile(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return user
