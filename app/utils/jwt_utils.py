from jose import jwt
from typing import Union, Any
from datetime import datetime, timedelta
from app.config import env


def create_token(data: Union[str, Any], expires_delta: int = None, secret_key: str = env.JWT_SECRET_KEY):
    """
    Create a JWT token with the provided data and optional expiration time.
    :param data: Data to be included in the token.
    :param expires_delta: Optional expiration time for the token.
    :param secret_key: Secret key to sign the token.
    :return: Encoded JWT token.
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(data)}
    encoded_jwt = jwt.encode(to_encode, secret_key, env.ALGORITHM)
    return encoded_jwt


def create_access_token(data: Union[str, Any], expires_delta: int = None):
    """Create an access token."""
    return create_token(data, expires_delta)


def create_refresh_token(data: Union[str, Any], expires_delta: int = None):
    """Create a refresh token."""
    return create_token(data, expires_delta, env.JWT_REFRESH_SECRET_KEY)


def decode_token(token: str, key: str):
    return jwt.decode(token=token, key=key, algorithms=[env.ALGORITHM])


def validate_date_token(payload):
    current_time = datetime.utcnow()
    token_expiration = datetime.fromtimestamp(payload["exp"])
    if current_time > token_expiration:
        return False
    return True
