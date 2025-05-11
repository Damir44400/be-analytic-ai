from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.interfaces.companies import ICompaniesDAO
from src.dashboard.domain.interfaces.branches import IBranchesDAO
from src.dashboard.infrastructure.daos.companies import CompaniesDAO
from src.dashboard.infrastructure.daos.branches import BranchesDAO


class DashboardDaosProviders(Provider):
    @provide(scope=Scope.REQUEST)
    def get_companies_dao(self, session: AsyncSession) -> ICompaniesDAO:
        return CompaniesDAO(session)

    @provide(scope=Scope.REQUEST)
    def get_company_branches_dao(self, session: AsyncSession) -> IBranchesDAO:
        return BranchesDAO(session)
