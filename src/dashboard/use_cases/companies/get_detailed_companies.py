from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.companies import CompanyEntity
from src.dashboard.domain.interfaces.companies import ICompanyGetByUserIdDAO


class GetDetailedCompaniesUseCase:
    def __init__(
            self,
            company_dao: ICompanyGetByUserIdDAO
    ):
        self._company_dao = company_dao

    async def execute(self, company_id: int, user_id: int) -> CompanyEntity:
        db_company = await self._company_dao.get_by_user_id(user_id=user_id, company_id=company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        return db_company
