from typing import Dict

from src.crm.domain.entities.employees import EmployeeEntity
from src.crm.domain.exceptions import NotFoundException, ForbiddenException
from src.crm.domain.interfaces.daos.emopoyees import (
    IEmployeeGetByIdDAO,
    IEmployeeGetByUserCompanyDAO,
    IEmployeeUpdateDAO
)
from src.crm.domain.interfaces.uow import IUoW


class EmployeeGateway(
    IEmployeeGetByIdDAO,
    IEmployeeGetByUserCompanyDAO,
    IEmployeeUpdateDAO
):
    ...


class UpdateEmployee:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: EmployeeGateway
    ):
        self._uow = uow
        self._employee_dao = employee_dao

    async def execute(
            self,
            employee_id: int,
            user_id: int,
            company_id: int,
            update_data: EmployeeEntity
    ) -> Dict[str, str]:
        actor = await self._employee_dao.get_by_user_and_company(user_id, company_id)
        if actor is None:
            raise NotFoundException("Actor not found in company")

        if not (actor.is_manager or actor.is_owner):
            raise ForbiddenException("Only managers or owners can update employees")
        target = await self._employee_dao.get_by_id(employee_id)
        if target is None:
            raise NotFoundException("Target employee not found")
        if target.is_manager and not actor.is_owner:
            raise ForbiddenException("Only owners can update managers")

        update_dict = update_data.to_dict()
        if update_dict.get("is_manager") and not actor.is_owner:
            raise ForbiddenException("Only owners can promote employees to manager")

        async with self._uow:
            await self._employee_dao.update(employee_id, update_data)

        return {
            "detail": f"Employee {employee_id} successfully updated"
        }
