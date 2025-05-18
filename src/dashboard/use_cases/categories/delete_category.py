from typing import Any, Dict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import BadRequestException
from src.dashboard.domain.interfaces.categories import (
    ICategoryDeleteDAO,
    ICategoryGetByIdDAO
)


class CategoryGateway(
    ICategoryDeleteDAO,
    ICategoryGetByIdDAO
):
    ...


class DeleteCategoryUseCase:
    def __init__(
            self,
            uow: IUoW,
            category_gateway: CategoryGateway
    ):
        self._uow = uow
        self._category_gateway = category_gateway

    async def execute(self, category_id: int) -> Dict[str, Any]:
        db_category = await self._category_gateway.get_by_id(category_id)
        if not db_category:
            raise BadRequestException("Category not exists with this given name")

        async with self._uow:
            await self._category_gateway.delete(
                db_category.id
            )
        return {"detail": "Category deleted"}
