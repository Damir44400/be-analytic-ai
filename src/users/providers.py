from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.config import Config
from src.core.domain.interfaces import IUoW
from src.users.domain.interfaces import IPasswordBcrypt, IJwtService
from src.users.domain.use_cases.login.interfaces import ILoginUseCase
from src.users.domain.use_cases.profile.interfaces import IProfileUseCase, IProfileUpdateUseCase
from src.users.domain.use_cases.refresh.interfaces import IRefreshUseCase
from src.users.domain.use_cases.register.interfaces import IRegisterUseCase
from src.users.infrastructure.dao import UserDAO, IUserDAO
from src.users.infrastructure.security import PasswordBcrypt, JwtService
from src.users.use_cases.login_use_case import LoginUseCase
from src.users.use_cases.profile_update_use_case import ProfileUpdateUseCase
from src.users.use_cases.profile_use_case import ProfileUseCase
from src.users.use_cases.refresh_use_case import RefreshUseCase
from src.users.use_cases.register_use_case import RegisterUseCase


class UserProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def get_user_dao(self, session: AsyncSession) -> IUserDAO:
        return UserDAO(session)

    @provide(scope=Scope.APP)
    def get_password_bcrypt(self) -> IPasswordBcrypt:
        return PasswordBcrypt()

    @provide(scope=Scope.APP)
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

    @provide(scope=Scope.REQUEST)
    def get_profile_use_case(
            self,
            user_dao: IUserDAO,
    ) -> IProfileUseCase:
        return ProfileUseCase(
            user_dao=user_dao,
        )

    @provide(scope=Scope.REQUEST)
    def get_refresh_use_case(
            self,
            jwt_service: IJwtService,
    ) -> IRefreshUseCase:
        return RefreshUseCase(
            jwt_service=jwt_service
        )

    @provide(scope=Scope.REQUEST)
    def get_profile_update_use_case(
            self,
            uow: IUoW,
            user_dao: IUserDAO,
    ) -> IProfileUpdateUseCase:
        return ProfileUpdateUseCase(uow=uow, user_dao=user_dao)
