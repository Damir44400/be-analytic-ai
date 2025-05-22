from dataclasses import asdict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException, BadRequestException
from src.crm.domain.entities.branches import CompanyBranchEntity
from src.crm.domain.interfaces.daos.branches import ICompanyBranchCreateDAO
from src.crm.domain.interfaces.daos.companies import ICompanyGetByUserIdDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserIdDAO, IEmployeeCreateDAO
from src.crm.domain.use_cases.branches import (
    CompanyBranchRegisterForm,
)
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class EmployeeGateway(
    IEmployeeGetByUserIdDAO,
    IEmployeeCreateDAO
):
    ...


class RegisterCompanyBranchUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: EmployeeGateway,
            company_dao: ICompanyGetByUserIdDAO,
            branch_dao: ICompanyBranchCreateDAO,
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._company_dao = company_dao
        self._branch_dao = branch_dao

    async def execute(self, form: CompanyBranchRegisterForm, user_id: int) -> CompanyBranchEntity:
        payload = asdict(form)
        db_employee = await self._employee_dao.get_by_user_id(user_id)

        if not db_employee:
            raise BadRequestException("Employee not found. You are not associated with any company.")
        elif db_employee.role != EmployeeRoleStatusEnum.OWNER.value:
            raise BadRequestException("You are not allowed to perform this action.")
        db_company = await self._company_dao.get_by_user_id(user_id, form.company_id)
        if not db_company:
            raise NotFoundException("Company not found")

        entity = CompanyBranchEntity(**payload)
        async with self._uow:
            return await self._branch_dao.create(entity)
