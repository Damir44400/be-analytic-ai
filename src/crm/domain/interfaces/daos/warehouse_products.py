from typing import Protocol, List
from src.crm.domain.entities.warehouse_product import WarehouseProductEntity


class IWarehouseProductAddDAO(Protocol):
    async def add(self, relation: WarehouseProductEntity) -> WarehouseProductEntity:
        ...


class IWarehouseProductDeleteDAO(Protocol):
    async def delete(self, product_id: int, warehouse_id: int) -> None:
        ...


class IWarehouseProductListByProductDAO(Protocol):
    async def list_by_product_id(self, product_id: int) -> List[WarehouseProductEntity]:
        ...


class IWarehouseProductListByWarehouseDAO(Protocol):
    async def list_by_warehouse_id(self, warehouse_id: int) -> List[WarehouseProductEntity]:
        ...


class IWarehouseProductDAO(
    IWarehouseProductAddDAO,
    IWarehouseProductDeleteDAO,
    IWarehouseProductListByProductDAO,
    IWarehouseProductListByWarehouseDAO,
):
    ...
