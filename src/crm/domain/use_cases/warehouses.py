from typing import Protocol, List

from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.entities.warehouse import WarehouseEntity


class IWarehouseCreateUseCase(Protocol):
    async def execute(self, data: WarehouseEntity, user_id: int) -> WarehouseEntity:
        ...


class IWarehouseUpdateUseCase(Protocol):
    async def execute(self, warehouse_id: int, user_id: int, data: WarehouseEntity) -> WarehouseEntity:
        ...


class IWarehouseDeleteUseCase(Protocol):
    async def execute(self, warehouse_id: int, user_id: int) -> WarehouseEntity:
        ...


class IWarehouseListUseCase(Protocol):
    async def execute(self, branch_id: int, user_id: int) -> List[WarehouseEntity]:
        ...


class ICompanyWarehouseUseCase(Protocol):
    async def execute(self, company_id: int) -> List[WarehouseEntity]:
        ...


class IGetWarehouseProductsUseCase(Protocol):
    async def execute(self, warehouse_id: int) -> List[ProductEntity]:
        ...
