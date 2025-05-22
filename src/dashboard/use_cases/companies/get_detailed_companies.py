from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.companies import CompanyEntity
from src.dashboard.domain.interfaces.daos.companies import ICompanyGetDAO


class GetDetailedCompaniesUseCase:
    def __init__(
            self,
            company_dao: ICompanyGetDAO
    ):
        self._company_dao = company_dao

    async def execute(self, company_id: int) -> CompanyEntity:
        db_company = await self._company_dao.get_by_id(company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        return db_company
