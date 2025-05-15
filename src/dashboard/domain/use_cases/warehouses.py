from typing import Protocol, List

from src.dashboard.domain.entities.warehouse import WarehouseEntity


class IWarehouseCreateUseCase(Protocol):
    async def execute(self, data: WarehouseEntity) -> WarehouseEntity:
        ...


class IWarehouseUpdateUseCase(Protocol):
    async def execute(self, warehouse_id: int, data: WarehouseEntity) -> WarehouseEntity:
        ...


class IWarehouseDeleteUseCase(Protocol):
    async def execute(self, warehouse_id: int) -> WarehouseEntity:
        ...


class IWarehouseDetailUseCase(Protocol):
    async def execute(self, warehouse_id: int) -> WarehouseEntity:
        ...


class IWarehouseListUseCase(Protocol):
    async def execute(self, branch_id: int) -> List[WarehouseEntity]:
        ...
