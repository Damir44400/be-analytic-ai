from typing import Protocol

from src.crm.domain.entities.product_category import ProductCategoryEntity


class IProductCategoryAddDAO(Protocol):
    async def add(self, relation: ProductCategoryEntity) -> ProductCategoryEntity:
        ...


class IProductCategoryDeleteDAO(Protocol):
    async def delete(self, product_id: int, category_id: int) -> None:
        ...


class IProductProductCategoryDAO(Protocol):
    async def get(self, product_id: int, category_id: int) -> ProductCategoryEntity:
        ...


class IProductCategoryDAO(
    IProductCategoryAddDAO,
    IProductCategoryDeleteDAO,
    IProductProductCategoryDAO
):
    ...
