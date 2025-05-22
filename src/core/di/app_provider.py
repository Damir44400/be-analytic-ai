from dishka import make_async_container, Provider, Scope, provide

from src.core.config import Config
from src.core.di.alchemy_provider import AlchemyProvider
from src.core.di.daos_provider import DashboardDaosProviders
from src.core.di.service_providers import ServiceProvider
from src.core.di.use_cases.branches_case_provider import BranchUseCasesProvider
from src.core.di.use_cases.companies_case_provider import CompanyUseCasesProvider
from src.core.di.use_cases.user_case_provider import UserUseCaseProvider
from src.core.di.use_cases.warehouse_case_provider import WarehouseUseCasesProvider


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
        DashboardDaosProviders(),
        UserUseCaseProvider(),
        CompanyUseCasesProvider(),
        BranchUseCasesProvider(),
        WarehouseUseCasesProvider(),
        ServiceProvider()
    )

    return container
