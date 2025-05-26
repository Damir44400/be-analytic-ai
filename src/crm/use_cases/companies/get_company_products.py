from typing import List

from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.exceptions import NotFoundException
from src.crm.domain.interfaces.daos.companies import ICompanyGetDAO
from src.crm.domain.interfaces.daos.products import IProductListByCompanyDAO


class ListProductsByCompanyUseCase:
    def __init__(
            self,
            company_dao: ICompanyGetDAO,
            product_dao: IProductListByCompanyDAO
    ):
        self._company_dao = company_dao
        self._product_dao = product_dao

    async def execute(self, company_id: int, filters: dict) -> List[ProductEntity]:
        db_company = await self._company_dao.get_by_id(company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        return await self._product_dao.list_by_company(company_id, filters)
