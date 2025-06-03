from typing import Dict

from src.crm.domain.exceptions import NotFoundException, ForbiddenException
from src.crm.domain.interfaces.daos.branches import (
    ICompanyBranchDeleteDAO, ICompanyBranchGetDAO
)
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserBranchDAO
from src.crm.domain.interfaces.uow import IUoW


class BranchGateway(
    ICompanyBranchDeleteDAO,
    ICompanyBranchGetDAO,
):
    ...


class DeleteCompanyBranchUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: IEmployeeGetByUserBranchDAO,
            branch_dao: BranchGateway,
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._branch_dao = branch_dao

    async def execute(self, branch_id: int, user_id: int) -> Dict[str, str]:
        db_employee = await self._employee_dao.get_by_user_branch(
            user_id=user_id,
            branch_id=branch_id
        )
        if not db_employee:
            raise NotFoundException("Employee not found")
        elif not db_employee.is_owner:
            raise ForbiddenException("You do not have access to this company")
        branch = await self._branch_dao.get_by_id(id=branch_id)
        if not branch:
            raise NotFoundException("Branch not found")
        async with self._uow:
            await self._branch_dao.delete(branch_id)

        return {"detail": "Branch deleted"}
