from dishka import make_async_container, Provider, Scope, provide

from src.core.config import Config
from src.core.di.alchemy_provider import AlchemyProvider
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
