from dataclasses import asdict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.companies import CompanyEntity
from src.dashboard.domain.interfaces.companies import ICompanyUpdateDAO, ICompanyGetByUserIdDAO
from src.dashboard.domain.use_cases.companies import CompanyUpdateForm


class GetUpdateCompanyGateway(
    ICompanyUpdateDAO,
    ICompanyGetByUserIdDAO
):
    ...


class UpdateCompanyUseCase:
    def __init__(
            self,
            uow: IUoW,
            company_dao: GetUpdateCompanyGateway
    ):
        self._uow = uow
        self._company_dao = company_dao

    async def execute(
            self,
            company_id: int,
            company: CompanyUpdateForm,
            user_id: int
    ) -> CompanyEntity:
        db_company = await self._company_dao.get_by_user_id(user_id, company_id)
        if not db_company:
            raise NotFoundException("Company for this user with this id not found")

        async with self._uow:
            refreshed_data = await self._company_dao.update(company_id, CompanyEntity(**asdict(company)))

        return refreshed_data
