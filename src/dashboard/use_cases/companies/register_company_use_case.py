from dataclasses import asdict
from typing import Dict

from src.core.domain.interfaces import IUoW
from ...domain.entities.companies import CompanyEntity
from ...domain.entities.company_branches import CompanyBranchEntity
from ...domain.interfaces.companies import ICompanyCreateDAO
from ...domain.interfaces.company_branches import (
    ICompanyBranchCreateDAO
)
from ...domain.use_cases.companies import (
    IRegisterCompanyUseCase,
    CompanyRegisterForm
)


class CompanyCreateGateway(ICompanyCreateDAO):
    ...


class CompanyBranchCreateGateway(ICompanyBranchCreateDAO):
    ...


class RegisterCompanyUseCase(IRegisterCompanyUseCase):
    def __init__(
            self,
            uow: IUoW,
            company_dao: CompanyCreateGateway,
            company_branch_dao: CompanyBranchCreateGateway
    ):
        self._uow = uow
        self._company_dao = company_dao
        self._company_branch_dao = company_branch_dao

    async def execute(self, company: CompanyRegisterForm, user_id: int) -> Dict[str, str]:
        company_data = asdict(company)
        branches_data = company_data.pop('branches', [])
        async with self._uow:
            await self._company_dao.create(CompanyEntity(**company_data))
            for branch_data in branches_data:
                await self._company_branch_dao.create(CompanyBranchEntity(**branch_data))

        return {
            "detail": "Successfully registered company"
        }
