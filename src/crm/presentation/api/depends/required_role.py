from functools import wraps
from typing import List

from src.crm.domain.exceptions import BadRequestException


def required_role(roles: List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            auth_user = kwargs.get("auth_user")

            if auth_user is None:
                raise BadRequestException("Authentication required")

            if auth_user.role not in roles:
                raise BadRequestException("You do not have permission to perform this action.")

            return await func(*args, **kwargs)

        return wrapper

    return decorator
