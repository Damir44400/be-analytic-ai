from typing import Protocol

from src.users.domain.entities import UserEntity, Token, Payload


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


class IPasswordBcrypt(Protocol):
    def verify_password(self, password: str, hash_password: str) -> bool:
        pass

    def hash_password(self, password: str) -> bytes:
        pass


class IJwtService(Protocol):
    def encode(self, payload: Payload, _is_refresh: bool = False) -> Token:
        pass

    def decode(self, token: str, _is_refresh: bool = False) -> Payload:
        pass
