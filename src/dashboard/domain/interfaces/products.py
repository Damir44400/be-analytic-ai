from typing import Protocol, List
from src.dashboard.domain.entities.products import ProductEntity


class IProductCreateDAO(Protocol):
    async def create(self, product: ProductEntity) -> ProductEntity:
        ...


class IProductUpdateDAO(Protocol):
    async def update(self, id: int, product: ProductEntity) -> ProductEntity:
        ...


class IProductDeleteDAO(Protocol):
    async def delete(self, id: int) -> None:
        ...


class IProductGetByIdDAO(Protocol):
    async def get_by_id(self, id: int) -> ProductEntity:
        ...


class IProductListAllDAO(Protocol):
    async def list_all(self) -> List[ProductEntity]:
        ...


class IProductsDAO(
    IProductCreateDAO,
    IProductUpdateDAO,
    IProductDeleteDAO,
    IProductGetByIdDAO,
    IProductListAllDAO,
):
    ...
