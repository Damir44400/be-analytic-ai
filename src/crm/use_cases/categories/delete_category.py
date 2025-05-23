from typing import Any, Dict

from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import BadRequestException
from src.crm.domain.interfaces.daos.categories import (
    ICategoryDeleteDAO,
    ICategoryGetByIdDAO
)
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class CategoryGateway(
    ICategoryDeleteDAO,
    ICategoryGetByIdDAO
):
    ...


class EmployeeGateway(
    IEmployeeGetByUserCompanyDAO
):
    ...


class DeleteCategoryUseCase:
    def __init__(
            self,
            uow: IUoW,
            category_gateway: CategoryGateway,
            employee_gateway: EmployeeGateway
    ):
        self._uow = uow
        self._category_gateway = category_gateway
        self._employee_gateway = employee_gateway

    async def execute(self, category_id: int, user_id: int) -> Dict[str, Any]:
        db_category = await self._category_gateway.get_by_id(category_id)
        if not db_category:
            raise BadRequestException("Category not exists with this given name")
        db_employee = await self._employee_gateway.get_by_user_and_company(user_id, db_category.id)
        if not db_employee or db_employee.role not in [
            EmployeeRoleStatusEnum.EMPLOYEE.value,
            EmployeeRoleStatusEnum.MANAGER.value
        ]:
            raise BadRequestException("Employee does not have required role or does not exist")
        async with self._uow:
            await self._category_gateway.delete(
                db_category.id
            )
        return {"detail": "Category deleted"}
