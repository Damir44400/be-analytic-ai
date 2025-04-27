from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from src.gateway.config import Config
from src.gateway.domain.interfaces import IUoW
from src.users.domain.interfaces import IPasswordBcrypt, IJwtService
from src.users.domain.use_cases.login.interfaces import ILoginUseCase
from src.users.domain.use_cases.register.interfaces import IRegisterUseCase
from src.users.infrastructure.dao import UserDAO, IUserDAO
from src.users.infrastructure.security import PasswordBcrypt, JwtService
from src.users.use_cases.login_use_case import LoginUseCase
from src.users.use_cases.register_use_case import RegisterUseCase


class UserProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def get_user_dao(self, session: AsyncSession) -> IUserDAO:
        return UserDAO(session)

    @provide(scope=Scope.REQUEST)
    def get_password_bcrypt(self) -> IPasswordBcrypt:
        return PasswordBcrypt()

    @provide(scope=Scope.REQUEST)
    def get_jwt_service(self, config: Config) -> IJwtService:
        return JwtService(config)

    @provide(scope=Scope.REQUEST)
    def get_login_use_case(
            self,
            user_dao: IUserDAO,
            password_bcrypt: IPasswordBcrypt,
            jwt_service: IJwtService
    ) -> ILoginUseCase:
        return LoginUseCase(
            user_dao=user_dao,
            password_bcrypt=password_bcrypt,
            jwt_service=jwt_service
        )

    @provide(scope=Scope.REQUEST)
    def get_register_use_case(
            self,
            uow: IUoW,
            user_dao: IUserDAO,
            password_bcrypt: IPasswordBcrypt,
    ) -> IRegisterUseCase:
        return RegisterUseCase(
            user_dao=user_dao,
            uow=uow,
            password_bcrypt=password_bcrypt,
        )
