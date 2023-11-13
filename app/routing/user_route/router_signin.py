from . import router, user_repo
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.depends import get_db
from app.schemas.token_schema import TokenPayload
from app.utils import (
    create_access_token,
    create_refresh_token,
    check_password
)


@router.post('/sign-in', summary="Create access and refresh tokens for user", response_model=TokenPayload)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_repo.get_user_by_username(db, form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['hashed_password']
    if not check_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }
