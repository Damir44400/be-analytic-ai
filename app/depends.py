import json

from pydantic import ValidationError
from sqlalchemy.orm import Session
from jose import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.database import SessionLocal
from app.repositories.user_repository import UserRepository
from app.config import env
from app.schemas.user_schema import User
from app.utils.jwt_utils import decode_token, validate_date_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/sign-in/access-token", scheme_name="JWT")
user_repo = UserRepository()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
) -> User:
    try:
        payload = decode_token(token, env.JWT_SECRET_KEY)
        if not validate_date_token(payload):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload_str = str(payload["sub"]).replace("'", "\"")
    payload_dict = json.loads(payload_str)
    user = user_repo.get_user_by_username(db, payload_dict["username"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return User(id=user.id, email=user.email, username=user.username, is_superuser=user.is_superuser,
                is_representative=user.is_representative)
