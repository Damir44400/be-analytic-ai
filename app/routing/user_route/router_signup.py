from app.depends import get_db
from . import router, user_repo
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.schemas.user_schema import UserProfile, UserRegistration
from app.utils import hash_password


@router.post('/sign-up', summary="Create new user", response_model=UserProfile)
async def create_user(data: UserRegistration, db: Session = Depends(get_db)):
    """User registration function"""
    user = user_repo.get_user_by_username(db, data.username)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exist"
        )
    user = user_repo.get_user_by_email(db, data.email)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = UserRegistration(
        email=data.email,
        username=data.username,
        password=hash_password(data.password)
    )
    user_repo.create_user(db, user)
    return user
