from typing import Protocol

from src.dashboard.domain.entities.users import UserEntity


class IUserGetByIdDAO(Protocol):
    async def get_user_by_id(self, user_id: int) -> UserEntity:
        pass


class IUserGetByEmailDAO(Protocol):
    async def get_user_by_email(self, email: str) -> UserEntity:
        pass


class IUserCreateUserDAO(Protocol):
    async def create_user(self, user: UserEntity) -> UserEntity:
        pass


class IUserUpdateUserDAO(Protocol):
    async def update_user(self, user_id: int, user: UserEntity) -> UserEntity:
        pass


class IUserDAO(
    IUserGetByIdDAO,
    IUserGetByEmailDAO,
    IUserCreateUserDAO,
    IUserUpdateUserDAO
):
    pass
