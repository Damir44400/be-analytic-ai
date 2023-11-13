from datetime import datetime
from typing import Union, Any
from pydantic import ValidationError
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.database import SessionLocal
from app.utils import jwt
from app.schemas.user_schema import UserProfile
from app.repositories.user_repository import UserRepository
from app.config import env
from schemas.token_schema import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/sign-in", scheme_name="JWT")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserProfile:
    try:
        payload = jwt.decode(
            token, env.JWT_SECRET_KEY, algorithms=[env.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user: Union[dict[str, Any], None] = UserRepository().get_user_by_username(db, payload.get("sub", None).username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return UserProfile(**user)
