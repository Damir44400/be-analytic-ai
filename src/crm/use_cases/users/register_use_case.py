from typing import Dict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import AlreadyExistsException
from src.crm.domain.entities.users import UserEntity
from src.crm.domain.interfaces.daos.users import IUserCreateUserDAO, IUserGetByEmailDAO
from src.crm.domain.interfaces.security.password_handler import IPasswordBcrypt
from src.crm.domain.use_cases.users import IRegisterUseCase


class UserGateway(
    IUserCreateUserDAO,
    IUserGetByEmailDAO
):
    ...


class RegisterUseCase(IRegisterUseCase):
    def __init__(
            self,
            uow: IUoW,
            user_dao: UserGateway,
            password_bcrypt: IPasswordBcrypt

    ):
        self._uow = uow
        self._user_dao = user_dao
        self._password_bcrypt = password_bcrypt

    async def execute(self, user: UserEntity) -> Dict[str, str]:
        db_user = await self._user_dao.get_user_by_email(user.email)
        if db_user:
            raise AlreadyExistsException("User with email already exists")
        hash_password = self._password_bcrypt.hash_password(user.password)
        user.password = hash_password
        async with self._uow:
            db_user = await self._user_dao.create_user(
                UserEntity(
                    email=user.email,
                    password=hash_password
                )
            )

        return {
            "user_id": db_user.id,
            "detail": "User created successfully",
        }
