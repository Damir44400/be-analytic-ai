from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import NotFoundException
from src.crm.domain.interfaces.daos.warehouses import (
    IWarehouseDeleteDAO,
    IWarehouseGetByUserDAO,
)


class WarehouseGateway(
    IWarehouseDeleteDAO,
    IWarehouseGetByUserDAO,
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

    async def execute(self, warehouse_id: int, user_id: int):
        warehouse = await self._warehouse_gateway.get_by_user(warehouse_id, user_id)
        if not warehouse:
            raise NotFoundException("Warehouse not found or does not exist")
        async with self._uow:
            await self._warehouse_gateway.delete(warehouse_id)

        return {"message": "Warehouse successfully deleted"}
