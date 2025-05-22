from dataclasses import asdict
from typing import Any, Dict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import BadRequestException
from src.crm.domain.entities.categories import CategoryEntity
from src.crm.domain.interfaces.daos.categories import (
    ICategoryGetByIdDAO,
    ICategoryUpdateDAO
)
from src.crm.domain.use_cases.categories import CategoryForm


class CategoryGateway(
    ICategoryUpdateDAO,
    ICategoryGetByIdDAO
):
    ...


class UpdateCategoryUseCase:
    def __init__(
            self,
            uow: IUoW,
            category_gateway: CategoryGateway
    ):
        self._uow = uow
        self._category_gateway = category_gateway

    async def execute(self, category_id: int, form: CategoryForm) -> Dict[str, Any]:
        db_category = await self._category_gateway.get_by_id(category_id)
        if not db_category:
            raise BadRequestException("Category not exists with this given name")

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
