from src.core.domain.interfaces import IUoW
from src.core.exceptions import AlreadyExistsException
from src.users.domain.entities import UserEntity
from src.users.domain.interfaces import IPasswordBcrypt
from src.users.domain.use_cases.register.entities import RegisterRequest, RegisterResponse
from src.users.domain.use_cases.register.interfaces import UserGetCreateGateway, IRegisterUseCase


class RegisterUseCase(IRegisterUseCase):
    def __init__(
            self,
            uow: IUoW,
            user_dao: UserGetCreateGateway,
            password_bcrypt: IPasswordBcrypt

    ):
        self._uow = uow
        self._user_dao = user_dao
        self._password_bcrypt = password_bcrypt

    async def execute(self, user: RegisterRequest) -> RegisterResponse:
        db_user = await self._user_dao.get_user_by_email(user.email)
        if db_user:
            raise AlreadyExistsException("User with email already exists")

        user.password = self._password_bcrypt.hash_password(user.password.encode("utf-8")).decode("utf-8")
        async with self._uow:
            db_user = await self._user_dao.create_user(
                UserEntity(
                    email=user.email,
                    password=user.password
                )
            )
        return RegisterResponse(
            user_id=db_user.id,
            detail="User created successfully",
        )
