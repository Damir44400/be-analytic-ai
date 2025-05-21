from typing import Protocol, List

from src.dashboard.domain.entities.categories import CategoryEntity


class ICategoryCreateDAO(Protocol):
    async def create(self, category: CategoryEntity) -> CategoryEntity:
        ...


class ICategoryUpdateDAO(Protocol):
    async def update(self, id: int, category: CategoryEntity) -> CategoryEntity:
        ...


class ICategoryDeleteDAO(Protocol):
    async def delete(self, id: int) -> None:
        ...


class ICategoryGetByIdDAO(Protocol):
    async def get_by_id(self, id: int) -> CategoryEntity:
        ...


class ICategoryListByCompanyIdDAO(Protocol):
    async def list_by_company_id(
            self,
            company_id: int
    ) -> List[CategoryEntity]:
        ...


class ICategoryGetByNameCompanyDAO(Protocol):
    async def get_by_name(self, name: str, company_id: int) -> CategoryEntity:
        ...


class ICategoriesDAO(
    ICategoryCreateDAO,
    ICategoryUpdateDAO,
    ICategoryDeleteDAO,
    ICategoryGetByIdDAO,
    ICategoryListByCompanyIdDAO,
    ICategoryGetByNameCompanyDAO
):
    ...
