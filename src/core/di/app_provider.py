from dishka import make_async_container, Provider, Scope, provide

from src.core.config import Config
from src.core.di.app.alchemy_provider import AlchemyProvider
from src.core.di.use_cases.companies_case_provider import CompanyUseCasesProvider
from src.core.di.app.daos_provider import DashboardDaosProviders
from src.core.di.app.users_providers import UserProvider


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
        DashboardDaosProviders(),
        CompanyUseCasesProvider(),
    )

    return container
