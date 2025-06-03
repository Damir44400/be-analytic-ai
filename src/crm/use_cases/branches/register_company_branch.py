from dataclasses import asdict

from src.crm.domain.entities.branches import CompanyBranchEntity
from src.crm.domain.exceptions import NotFoundException, ForbiddenException
from src.crm.domain.interfaces.daos.branches import ICompanyBranchCreateDAO
from src.crm.domain.interfaces.daos.companies import ICompanyGetByUserIdDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.use_cases.branches import (
    CompanyBranchRegisterForm,
)


class RegisterCompanyBranchUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: IEmployeeGetByUserCompanyDAO,
            company_dao: ICompanyGetByUserIdDAO,
            branch_dao: ICompanyBranchCreateDAO,
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._company_dao = company_dao
        self._branch_dao = branch_dao

    async def execute(self, form: CompanyBranchRegisterForm, user_id: int) -> CompanyBranchEntity:
        payload = asdict(form)
        db_company = await self._company_dao.get_by_user_id(user_id, form.company_id)
        if not db_company:
            raise NotFoundException("Company not found")

        employee = await self._employee_dao.get_by_user_and_company(user_id, form.company_id)
        if not employee:
            raise NotFoundException("Employee not found")
        elif employee.is_manager_or_owner:
            raise ForbiddenException("You don't have permission to perform this action")
        entity = CompanyBranchEntity(**payload)
        async with self._uow:
            return await self._branch_dao.create(entity)
