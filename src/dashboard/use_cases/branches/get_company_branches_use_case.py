from typing import List

from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.branches import CompanyBranchEntity
from src.dashboard.domain.interfaces.branches import ICompanyBranchGetByCompanyDAO
from src.dashboard.domain.interfaces.companies import ICompanyGetDAO
from src.dashboard.domain.use_cases.branches import IGetCompanyBranchesUseCase


class GetCompanyBranchesUseCase(IGetCompanyBranchesUseCase):
    def __init__(
            self,
            company_dao: ICompanyGetDAO,
            branch_dao: ICompanyBranchGetByCompanyDAO
    ):
        self._company_dao = company_dao
        self._branch_dao = branch_dao

    async def execute(self, company_id: int) -> List[CompanyBranchEntity]:
        db_company = await self._company_dao.get_by_id(company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        return await self._branch_dao.get_by_company_id(company_id=company_id)
