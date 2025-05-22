from dishka import Provider, provide, Scope

from src.core.config import Config
from src.dashboard.domain.interfaces.security.jwt_handler import IJwtService
from src.dashboard.domain.interfaces.security.password_handler import IPasswordBcrypt
from src.dashboard.infrastructure.services.jwt_handler import JwtService
from src.dashboard.infrastructure.services.password_handler import PasswordBcrypt


class ServiceProvider(Provider):

    @provide(scope=Scope.APP)
    def get_password_bcrypt(self) -> IPasswordBcrypt:
        return PasswordBcrypt()

    @provide(scope=Scope.APP)
    def get_jwt_service(self, config: Config) -> IJwtService:
        return JwtService(config)
