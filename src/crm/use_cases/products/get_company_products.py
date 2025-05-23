from typing import List

from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.interfaces.daos.products import IProductListByCompanyDAO


class ListProductsByCompanyUseCase:
    def __init__(self, product_dao: IProductListByCompanyDAO):
        self._product_dao = product_dao

    async def execute(self, company_id: int) -> List[ProductEntity]:
        return await self._product_dao.list_by_company(company_id)
