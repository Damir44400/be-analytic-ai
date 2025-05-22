from typing import List

from src.dashboard.domain.entities.companies import CompanyEntity
from src.dashboard.domain.interfaces.daos.companies import ICompaniesListByUsersDAO


class GetUserCompaniesUseCase:
    def __init__(
            self,
            company_dao: ICompaniesListByUsersDAO,
    ):
        self._company_dao = company_dao

    async def execute(self, user_id: int) -> List[CompanyEntity]:
        user_companies = await self._company_dao.user_companies(user_id)
        return user_companies
