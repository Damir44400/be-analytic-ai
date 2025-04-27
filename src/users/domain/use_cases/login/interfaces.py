from typing import Protocol

from src.users.domain.interfaces import (
    IUserGetByEmailDAO
)
from src.users.domain.use_cases.login.entities import LoginRequest
from src.users.domain.use_cases.login.entities import TokenResponse


class UserGetGateway(
    IUserGetByEmailDAO,
):
    pass


class ILoginUseCase(Protocol):
    async def execute(self, user: LoginRequest) -> TokenResponse:
        pass
