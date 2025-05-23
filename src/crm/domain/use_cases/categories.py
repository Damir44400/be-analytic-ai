from typing import Protocol, List, Dict, Any

from src.crm.domain.entities.categories import CategoryEntity


class ICategoryCreateUseCase(Protocol):
    async def execute(
            self,
            body: CategoryEntity,
            user_id: int
    ) -> CategoryEntity:
        ...


class ICategoryUpdateUseCase(Protocol):
    async def execute(
            self,
            category_id: int,
            body: CategoryEntity,
            user_id: int
    ) -> CategoryEntity:
        ...


class ICategoryDeleteUseCase(Protocol):
    async def execute(
            self,
            category_id: int,
            user_id: int
    ) -> Dict[str, Any]:
        ...


class ICompanyCategoryListUseCase(Protocol):
    async def execute(
            self,
            company_id: int
    ) -> List[CategoryEntity]:
        ...
