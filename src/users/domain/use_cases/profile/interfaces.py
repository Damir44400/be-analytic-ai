from typing import Protocol

from src.users.domain.entities import UserEntity
from src.users.domain.interfaces import IUserGetByIdDAO, IUserUpdateUserDAO
from src.users.domain.use_cases.profile.entities import Profile


class UserGetGateway(
    IUserGetByIdDAO
):
    pass


class UserGetUpdateGateway(
    IUserGetByIdDAO,
    IUserUpdateUserDAO
):
    pass


class IProfileUseCase(Protocol):
    async def execute(self, user_id: int) -> UserEntity:
        pass


class IProfileUpdateUseCase(Protocol):
    async def execute(self, user_id: int, profile: Profile) -> UserEntity:
        pass
