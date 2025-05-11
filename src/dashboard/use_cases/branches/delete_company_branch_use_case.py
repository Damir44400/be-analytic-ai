from typing import Dict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.dashboard.domain.interfaces.branches import (
    ICompanyBranchGetByUserIdDAO,
    ICompanyBranchDeleteDAO
)
from src.dashboard.domain.use_cases.branches import IDeleteCompanyBranchUseCase


class Gateway(ICompanyBranchDeleteDAO, ICompanyBranchGetByUserIdDAO):
    ...


class DeleteCompanyBranchUseCase(IDeleteCompanyBranchUseCase):
    def __init__(
            self,
            uow: IUoW,
            dao: Gateway,
    ):
        self._uow = uow
        self._dao = dao

    async def execute(self, branch_id: int, user_id: int) -> Dict[str, str]:
        branch = await self._dao.get_by_user_id(user_id, branch_id)
        if not branch:
            raise NotFoundException("Branch not found")

        async with self._uow:
            await self._dao.delete(branch_id)
        return {"detail": "Branch deleted"}
