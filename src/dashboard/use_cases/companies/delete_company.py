from typing import Dict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException, BadRequestException
from src.dashboard.domain.interfaces.daos.companies import ICompanyDeleteDAO, ICompanyGetByUserIdDAO
from src.dashboard.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.dashboard.infrastructure.models.employees import EmployeeRoleStatusEnum


class CompanyGateway(
    ICompanyDeleteDAO,
    ICompanyGetByUserIdDAO
):
    pass


class DeleteCompanyUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: IEmployeeGetByUserCompanyDAO,
            company_dao: CompanyGateway,
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._company_dao = company_dao

    async def execute(self, company_id: int, user_id: int) -> Dict[str, str]:
        db_employee = await self._employee_dao.get_by_user_and_company(user_id, company_id)
        if not db_employee or db_employee.role != EmployeeRoleStatusEnum.OWNER:
            raise BadRequestException("You do not have permission to perform this action.")
        db_company = await self._company_dao.get_by_user_id(user_id=user_id, company_id=company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        async with self._uow:
            await self._company_dao.delete(company_id=company_id)
        return {"detail": "Company deleted"}
