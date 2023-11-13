from . import router, user_repo
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from app.depends import get_db
from app.schemas.token_schema import TokenSchema
from app.utils.jwt_utils import (
    create_access_token,
    create_refresh_token,
)
from app.utils.security_utils import check_password
from app.config import env


@router.post('/sign-in/access-token', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_repo.get_user_by_username(db, form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    if not check_password(password=form_data.password, password_in_db=user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    access_token = create_access_token({"user_id": user.id, "username": user.username})
    refresh_token = create_refresh_token({"user_id": user.id, "username": user.username})
    response.set_cookie('access_token', access_token, env.ACCESS_TOKEN_EXPIRE_MINUTES,
                        env.ACCESS_TOKEN_EXPIRE_MINUTES, '/', None, False, True, 'lax')
    response.set_cookie('refresh_token', refresh_token,
                        env.REFRESH_TOKEN_EXPIRE_MINUTES, env.REFRESH_TOKEN_EXPIRE_MINUTES, '/', None, False, True,
                        'lax')
    response.set_cookie('logged_in', 'True', env.ACCESS_TOKEN_EXPIRE_MINUTES,
                        env.ACCESS_TOKEN_EXPIRE_MINUTES, '/', None, False, False, 'lax')
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
