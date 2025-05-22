from dataclasses import asdict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException, BadRequestException
from src.crm.domain.entities.companies import CompanyEntity
from src.crm.domain.interfaces.daos.companies import ICompanyUpdateDAO, ICompanyGetByUserIdDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.use_cases.companies import CompanyUpdateForm
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class GetUpdateCompanyGateway(
    ICompanyUpdateDAO,
    ICompanyGetByUserIdDAO
):
    ...


class UpdateCompanyUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: IEmployeeGetByUserCompanyDAO,
            company_dao: GetUpdateCompanyGateway
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._company_dao = company_dao

    async def execute(
            self,
            company_id: int,
            company: CompanyUpdateForm,
            user_id: int
    ) -> CompanyEntity:
        db_employee = await self._employee_dao.get_by_user_and_company(user_id, company_id)
        if not db_employee or db_employee.role != EmployeeRoleStatusEnum.OWNER:
            raise BadRequestException("You do not have permission to perform this action.")
        db_company = await self._company_dao.get_by_user_id(user_id, company_id)
        if not db_company:
            raise NotFoundException("Company for this user with this id not found")

        async with self._uow:
            refreshed_data = await self._company_dao.update(company_id, CompanyEntity(**asdict(company)))

        return refreshed_data
