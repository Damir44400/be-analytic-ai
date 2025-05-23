from dataclasses import asdict
from typing import Dict

from src.core.domain.interfaces import IUoW
from src.crm.domain.interfaces.daos.branches import (
    ICompanyBranchCreateDAO
)
from src.crm.domain.interfaces.daos.companies import ICompanyCreateDAO
from ...domain.entities.branches import CompanyBranchEntity
from ...domain.entities.companies import CompanyEntity
from ...domain.entities.employees import EmployeeEntity
from ...domain.interfaces.daos.emopoyees import (
    IEmployeeCreateDAO,
    IEmployeeGetByUserCompanyDAO
)
from ...domain.use_cases.companies import (
    CompanyRegisterForm
)
from ...infrastructure.models.employees import EmployeeRoleStatusEnum


class EmployeeGateway(
    IEmployeeCreateDAO,
    IEmployeeGetByUserCompanyDAO
):
    ...


class CompanyCreateGateway(ICompanyCreateDAO):
    ...


class CompanyBranchCreateGateway(ICompanyBranchCreateDAO):
    ...


class RegisterCompanyUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_gateway: EmployeeGateway,
            company_dao: CompanyCreateGateway,
            company_branch_dao: CompanyBranchCreateGateway
    ):
        self._uow = uow
        self._employee_gateway = employee_gateway
        self._company_dao = company_dao
        self._company_branch_dao = company_branch_dao

    async def execute(self, company: CompanyRegisterForm, user_id: int) -> Dict[str, str]:
        company_data = asdict(company)
        company_data['user_id'] = user_id
        if company_data.get('company_website', None):
            company_data['company_website'] = str(company_data['company_website'])
        branches_data = company_data.pop('branches', [])
        async with self._uow:
            company = await self._company_dao.create(CompanyEntity(**company_data))
            for branch_data in branches_data:
                branch_data['company_id'] = company.id
                await self._company_branch_dao.create(CompanyBranchEntity(**branch_data))
            await self._employee_gateway.create(
                EmployeeEntity(
                    user_id=user_id,
                    company_id=company.id,
                    role=EmployeeRoleStatusEnum.OWNER.value
                )
            )
        return {
            "detail": "Successfully registered company"
        }
