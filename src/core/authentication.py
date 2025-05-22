import jwt
from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends
from fastapi.security.http import HTTPBearer, HTTPAuthorizationCredentials

from src.core.exceptions import UnauthorizedException
from src.dashboard.domain.entities.users import UserEntity
from src.dashboard.domain.interfaces.daos.users import IUserDAO
from src.dashboard.domain.interfaces.security.jwt_handler import IJwtService

bearer = HTTPBearer()


@inject
async def get_current_user(
        jwt_service: FromDishka[IJwtService],
        user_dao: FromDishka[IUserDAO],
        token: HTTPAuthorizationCredentials = Depends(bearer),
) -> UserEntity:
    if not token.credentials:
        raise UnauthorizedException("Invalid credentials")
    try:
        payload = jwt_service.decode(token.credentials)
    except jwt.ExpiredSignatureError:
        raise UnauthorizedException("Expired token")
    except jwt.DecodeError:
        raise UnauthorizedException("Invalid token")

    db_user = await user_dao.get_user_by_id(payload.user_id)
    if not db_user:
        raise UnauthorizedException("User not found")

    return db_user
