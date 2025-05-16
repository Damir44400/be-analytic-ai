from dataclasses import asdict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.branches import CompanyBranchEntity
from src.dashboard.domain.interfaces.branches import (
    ICompanyBranchGetByUserIdDAO,
    ICompanyBranchUpdateDAO,
)
from src.dashboard.domain.use_cases.branches import (
    IUpdateCompanyBranchUseCase,
    CompanyBranchUpdateForm
)


class Gateway(
    ICompanyBranchUpdateDAO,
    ICompanyBranchGetByUserIdDAO
):
    pass


class UpdateCompanyBranchUseCase(IUpdateCompanyBranchUseCase):
    def __init__(
            self,
            uow: IUoW,
            dao: Gateway,
    ):
        self._uow = uow
        self._dao = dao

    async def execute(
            self,
            branch_id: int,
            form: CompanyBranchUpdateForm,
            user_id: int,
    ) -> CompanyBranchEntity:
        existing = await self._dao.get_by_user_id(user_id, branch_id)
        if not existing:
            raise NotFoundException("Branch not found")
        update_data = CompanyBranchEntity(asdict(form))
        async with self._uow:
            return await self._dao.update(branch_id, update_data)
