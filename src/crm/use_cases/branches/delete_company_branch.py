from typing import Dict

from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import NotFoundException, BadRequestException
from src.crm.domain.interfaces.daos.branches import (
    ICompanyBranchDeleteDAO, ICompanyBranchGetDAO
)
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserIdDAO
from src.crm.domain.use_cases.branches import IDeleteCompanyBranchUseCase
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class EmployeeGateway(
    IEmployeeGetByUserIdDAO
):
    ...


class BranchGateway(
    ICompanyBranchDeleteDAO,
    ICompanyBranchGetDAO,
):
    ...


class DeleteCompanyBranchUseCase(IDeleteCompanyBranchUseCase):
    def __init__(
            self,
            uow: IUoW,
            employee_dao: EmployeeGateway,
            branch_dao: BranchGateway,
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._branch_dao = branch_dao

    async def execute(self, branch_id: int, user_id: int) -> Dict[str, str]:
        db_employee = await self._employee_dao.get_by_user_id(user_id=user_id)
        if db_employee.role != EmployeeRoleStatusEnum.OWNER:
            raise BadRequestException("You are not the owner of the company")
        branch = await self._branch_dao.get_by_id(id=branch_id)
        if not branch:
            raise NotFoundException("Branch not found")
        async with self._uow:
            await self._branch_dao.delete(branch_id)

        return {"detail": "Branch deleted"}
