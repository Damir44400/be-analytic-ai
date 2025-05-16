from dataclasses import asdict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.branches import CompanyBranchEntity
from src.dashboard.domain.interfaces.branches import ICompanyBranchCreateDAO
from src.dashboard.domain.interfaces.companies import ICompanyGetByUserIdDAO
from src.dashboard.domain.use_cases.branches import (
    IRegisterCompanyBranchUseCase,
    CompanyBranchRegisterForm,
)


class RegisterCompanyBranchUseCase(IRegisterCompanyBranchUseCase):
    def __init__(
            self,
            uow: IUoW,
            company_dao: ICompanyGetByUserIdDAO,
            branch_dao: ICompanyBranchCreateDAO,
    ):
        self._uow = uow
        self._company_dao = company_dao
        self._branch_dao = branch_dao

    async def execute(self, form: CompanyBranchRegisterForm, user_id: int) -> CompanyBranchEntity:
        payload = asdict(form)
        db_company = await self._company_dao.get_by_user_id(user_id, form.company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        entity = CompanyBranchEntity(**payload)
        async with self._uow:
            return await self._branch_dao.create(entity)
