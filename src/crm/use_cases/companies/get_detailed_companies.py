from dataclasses import dataclass

from src.crm.domain.entities.companies import CompanyEntity
from src.crm.domain.exceptions import NotFoundException
from src.crm.domain.interfaces.daos.companies import ICompanyGetDAO
from src.crm.domain.interfaces.daos.products import IProductListByCompanyDAO
from src.crm.domain.interfaces.daos.warehouses import IWarehousesGetByCompany


@dataclass
class DetailedResponse:
    total_warehouses: int
    total_products: int


class GetDetailedCompaniesUseCase:
    def __init__(
            self,
            company_dao: ICompanyGetDAO,
            warehouse_dao: IWarehousesGetByCompany,
            products_dao: IProductListByCompanyDAO
    ):
        self._company_dao = company_dao
        self._warehouse_dao = warehouse_dao
        self._products_dao = products_dao

    async def execute(self, company_id: int) -> DetailedResponse:
        db_company = await self._company_dao.get_by_id(company_id)
        if not db_company:
            raise NotFoundException("Company not found")

        total_warehouses = len(await self._warehouse_dao.get_by_company(company_id))
        total_products = len(await self._products_dao.list_by_company(company_id))
        return DetailedResponse(
            **db_company.to_dict(),
            total_products=total_products,
            total_warehouses=total_warehouses
        )
