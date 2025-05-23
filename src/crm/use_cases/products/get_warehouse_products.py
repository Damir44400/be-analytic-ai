from typing import List

from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.interfaces.daos.products import IProductListByWarehouseDAO


class ListProductsByWarehouseUseCase:
    def __init__(self, product_dao: IProductListByWarehouseDAO, company_id: int):
        self._product_dao = product_dao
        self._company_id = company_id

    async def execute(self, warehouse_id: int) -> List[ProductEntity]:
        return await self._product_dao.list_by_warehouse(warehouse_id)