from typing import Protocol, List
from src.dashboard.domain.entities.warehouse_transfer import WarehouseTransferEntity


class IWarehouseTransferCreateDAO(Protocol):
    async def create(self, transfer: WarehouseTransferEntity) -> WarehouseTransferEntity:
        ...


class IWarehouseTransferGetByIdDAO(Protocol):
    async def get_by_id(self, id: int) -> WarehouseTransferEntity:
        ...


class IWarehouseTransferListByProductDAO(Protocol):
    async def list_by_product(self, product_id: int) -> List[WarehouseTransferEntity]:
        ...


class IWarehouseTransferListByWarehouseDAO(Protocol):
    async def list_by_warehouse(self, warehouse_id: int) -> List[WarehouseTransferEntity]:
        ...


class IWarehouseTransfersDAO(
    IWarehouseTransferCreateDAO,
    IWarehouseTransferGetByIdDAO,
    IWarehouseTransferListByProductDAO,
    IWarehouseTransferListByWarehouseDAO,
):
    ...
