from dataclasses import asdict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.crm.domain.entities.warehouse import WarehouseEntity
from src.crm.domain.interfaces.daos.warehouses import IWarehouseUpdateDAO, IWarehouseGetByIdDAO


class WarehouseGateway(
    IWarehouseUpdateDAO,
    IWarehouseGetByIdDAO,
):
    ...


class UpdateWarehouseUseCase:
    def __init__(
            self,
            uow: IUoW,
            warehouse_gateway: WarehouseGateway
    ):
        self._uow = uow
        self._warehouse_gateway = warehouse_gateway

    async def execute(self, warehouse_id: int, user_id: int, form: WarehouseEntity):
        warehouse = await self._warehouse_gateway.get_by_id(warehouse_id)
        if not warehouse:
            raise NotFoundException("Warehouse not found")
        async with self._uow:
            updated_warehouse = await self._warehouse_gateway.update(
                warehouse_id,
                WarehouseEntity(**asdict(form))
            )

        return updated_warehouse
