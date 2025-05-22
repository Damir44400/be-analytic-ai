from dishka import Provider, provide, Scope

from src.core.domain.interfaces import IUoW
from src.dashboard.domain.interfaces.daos.users import IUserDAO
from src.dashboard.domain.interfaces.security.jwt_handler import IJwtService
from src.dashboard.domain.interfaces.security.password_handler import IPasswordBcrypt
from src.dashboard.domain.use_cases.users import (
    ILoginUseCase,
    IRegisterUseCase,
    IProfileUseCase,
    IRefreshUseCase,
    IProfileUpdateUseCase
)
from src.dashboard.use_cases.users.login_use_case import LoginUseCase
from src.dashboard.use_cases.users.profile_update_use_case import ProfileUpdateUseCase
from src.dashboard.use_cases.users.profile_use_case import ProfileUseCase
from src.dashboard.use_cases.users.refresh_use_case import RefreshUseCase
from src.dashboard.use_cases.users.register_use_case import RegisterUseCase


class UserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_login_use_case(
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
    async def get_register_use_case(
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
    async def get_profile_use_case(
            self,
            user_dao: IUserDAO,
    ) -> IProfileUseCase:
        return ProfileUseCase(
            user_dao=user_dao,
        )

    @provide(scope=Scope.REQUEST)
    async def get_refresh_use_case(
            self,
            jwt_service: IJwtService,
    ) -> IRefreshUseCase:
        return RefreshUseCase(
            jwt_service=jwt_service
        )

    @provide(scope=Scope.REQUEST)
    async def get_profile_update_use_case(
            self,
            uow: IUoW,
            user_dao: IUserDAO,
    ) -> IProfileUpdateUseCase:
        return ProfileUpdateUseCase(uow=uow, user_dao=user_dao)
