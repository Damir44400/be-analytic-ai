from typing import Dict

from src.crm.domain.exceptions import NotFoundException, ForbiddenException
from src.crm.domain.interfaces.daos.emopoyees import (
    IEmployeeDeleteDAO,
    IEmployeeGetByIdDAO,
    IEmployeeGetByUserCompanyDAO,
)
from src.crm.domain.interfaces.uow import IUoW


class EmployeeGateway(
    IEmployeeGetByIdDAO,
    IEmployeeGetByUserCompanyDAO,
    IEmployeeDeleteDAO
):
    ...


class DeleteEmployee:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: EmployeeGateway
    ):
        self._uow = uow
        self._employee_dao = employee_dao

    async def execute(self, employee_id: int, user_id: int, company_id: int) -> Dict[str, str]:
        actor = await self._employee_dao.get_by_user_and_company(user_id, company_id)
        if actor is None:
            raise NotFoundException("Actor not found in company")
        if not (actor.is_manager or actor.is_owner):
            raise ForbiddenException("Only managers or owners can delete employees")

        target = await self._employee_dao.get_by_id(employee_id)
        if target is None:
            raise NotFoundException("Target employee not found")

        if actor.id == target.id:
            raise ForbiddenException("You cannot delete yourself")

        if target.is_manager and not actor.is_owner:
            raise ForbiddenException("Only owners can delete managers")

        async with self._uow:
            await self._employee_dao.delete(employee_id)

        return {
            "detail": f"Employee with ID {employee_id} has been successfully deleted"
        }
