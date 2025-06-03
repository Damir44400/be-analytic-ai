from dataclasses import asdict
from typing import Any, Dict

from src.crm.domain.entities.categories import CategoryEntity
from src.crm.domain.exceptions import ForbiddenException, NotFoundException
from src.crm.domain.interfaces.daos.categories import (
    ICategoryGetByIdDAO,
    ICategoryUpdateDAO
)
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCategoryDAO
from src.crm.domain.interfaces.uow import IUoW


class CategoryGateway(
    ICategoryUpdateDAO,
    ICategoryGetByIdDAO
):
    ...


class UpdateCategoryUseCase:
    def __init__(
            self,
            uow: IUoW,
            category_gateway: CategoryGateway,
            employee_gateway: IEmployeeGetByUserCategoryDAO,
    ):
        self._uow = uow
        self._category_gateway = category_gateway
        self._employee_gateway = employee_gateway

    async def execute(self, category_id: int, form: CategoryEntity, user_id: int) -> Dict[str, Any]:
        db_employee = await self._employee_gateway.get_by_user_and_category(
            user_id,
            category_id
        )
        if not db_employee or not db_employee.is_manager_or_owner:
            raise ForbiddenException("Employee does not have required role or does not exist")
        db_category = await self._category_gateway.get_by_id(category_id)
        if not db_category:
            raise NotFoundException("Category not exists with this given name")
        async with self._uow:
            await self._category_gateway.update(
                db_category.id,
                CategoryEntity(
                    **asdict(
                        form
                    )
                )
            )
        return {"detail": "Category deleted"}
