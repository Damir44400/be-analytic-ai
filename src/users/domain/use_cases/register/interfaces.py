from typing import Protocol

from src.users.domain.interfaces import (
    IUserGetByEmailDAO, IUserCreateUserDAO
)
from src.users.domain.use_cases.register.entities import RegisterRequest, RegisterResponse


class UserGetCreateGateway(
    IUserGetByEmailDAO,
    IUserCreateUserDAO
):
    pass


class IRegisterUseCase(Protocol):
    async def execute(self, user: RegisterRequest) -> RegisterResponse:
        pass
