from typing import Protocol, List
from src.dashboard.domain.entities.product_category import ProductCategoryEntity


class IProductCategoryAddDAO(Protocol):
    async def add(self, relation: ProductCategoryEntity) -> ProductCategoryEntity:
        ...


class IProductCategoryDeleteDAO(Protocol):
    async def delete(self, product_id: int, category_id: int) -> None:
        ...


class IProductCategoryListByProductDAO(Protocol):
    async def list_by_product_id(self, product_id: int) -> List[ProductCategoryEntity]:
        ...


class IProductCategoryListByCategoryDAO(Protocol):
    async def list_by_category_id(self, category_id: int) -> List[ProductCategoryEntity]:
        ...


class IProductCategoryDAO(
    IProductCategoryAddDAO,
    IProductCategoryDeleteDAO,
    IProductCategoryListByProductDAO,
    IProductCategoryListByCategoryDAO,
):
    ...
