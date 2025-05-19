from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.dashboard.domain.interfaces.warehouses import (
    IWarehouseDeleteDAO,
    IWarehouseGetByIdDAO
)


class WarehouseGateway(
    IWarehouseDeleteDAO,
    IWarehouseGetByIdDAO,
):
    ...


class DeleteWarehouseUseCase:
    def __init__(
            self,
            uow: IUoW,
            warehouse_gateway: WarehouseGateway
    ):
        self._uow = uow
        self._warehouse_gateway = warehouse_gateway

    async def execute(self, warehouse_id: int):
        warehouse = await self._warehouse_gateway.get_by_id(warehouse_id)
        if not warehouse:
            raise NotFoundException("Warehouse not found")
        async with self._uow:
            await self._warehouse_gateway.delete(warehouse_id)

        return {"message": "Warehouse successfully deleted"}
