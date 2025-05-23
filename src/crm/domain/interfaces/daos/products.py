from typing import Protocol, List

from src.crm.domain.entities.products import ProductEntity


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


class IProductListByCompanyDAO(Protocol):
    async def list_by_company(self, company_id: int) -> List[ProductEntity]:
        ...


class IProductListByWarehouseDAO(Protocol):
    async def list_by_warehouse(self, warehouse_id: int) -> List[ProductEntity]:
        ...


class IProductsDAO(
    IProductCreateDAO,
    IProductUpdateDAO,
    IProductDeleteDAO,
    IProductGetByIdDAO,
    IProductListByCompanyDAO,
    IProductListByWarehouseDAO
):
    ...
