from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.interfaces.daos.branches import IBranchesDAO
from src.dashboard.domain.interfaces.daos.companies import ICompaniesDAO
from src.dashboard.domain.interfaces.daos.warehouses import IWarehousesDAO
from src.dashboard.infrastructure.daos.branches import BranchesDAO
from src.dashboard.infrastructure.daos.companies import CompaniesDAO
from src.dashboard.infrastructure.daos.warehouses import WarehousesDAO


class DashboardDaosProviders(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_companies_dao(self, session: AsyncSession) -> ICompaniesDAO:
        return CompaniesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_company_branches_dao(self, session: AsyncSession) -> IBranchesDAO:
        return BranchesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_warehouses_dao(self, session: AsyncSession) -> IWarehousesDAO:
        return WarehousesDAO(session)
