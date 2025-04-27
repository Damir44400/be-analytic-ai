from dishka import make_async_container, Provider, Scope, provide

from src.gateway.config import Config
from src.gateway.di.alchemy_provider import AlchemyProvider
from src.users.domain.providers import UserProvider


class AppProvider(Provider):
    scope = Scope.APP

    @provide
    def get_config(self) -> Config:
        return Config()


def create_container():
    """Создаёт главный DI-контейнер"""
    container = make_async_container(
        AppProvider(),
        AlchemyProvider(),
        UserProvider(),
    )

    return container
