from typing import List

from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.exceptions import NotFoundException
from src.crm.domain.interfaces.daos.products import IProductListByWarehouseDAO
from src.crm.domain.interfaces.daos.warehouses import IWarehouseGetByIdDAO


class GetWarehouseProductsUseCase:
    def __init__(
            self,
            warehouse_dao: IWarehouseGetByIdDAO,
            products_dao: IProductListByWarehouseDAO,
    ):
        self._warehouse_dao = warehouse_dao
        self._products_dao = products_dao

    async def execute(self, warehouse_id: int) -> List[ProductEntity]:
        warehouse = await self._warehouse_dao.get_by_id(warehouse_id)
        if not warehouse:
            raise NotFoundException("Warehouse not found")

        products = await self._products_dao.list_by_warehouse(warehouse.id)
        return products
