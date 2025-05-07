from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.infrastructure.daos.companies import ICompaniesDAO, CompaniesDAO


class DaoProviders(Provider):
    @provide(scope=Scope.REQUEST)
    def get_companies_dao(self, session: AsyncSession) -> ICompaniesDAO:
        return CompaniesDAO(session)
