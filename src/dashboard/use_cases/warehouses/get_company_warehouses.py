from typing import List

from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.warehouse import WarehouseEntity
from src.dashboard.domain.interfaces.daos.companies import ICompanyGetDAO
from src.dashboard.domain.interfaces.daos.warehouses import IWarehousesGetByCompany


class CompanyGateway(ICompanyGetDAO):
    pass


class WarehouseGateway(
    IWarehousesGetByCompany
):
    pass


class CompanyWarehousesListUseCase:
    def __init__(
            self,
            company_gateway: CompanyGateway,
            warehouse_gateway: WarehouseGateway
    ):
        self._company_gateway = company_gateway
        self._warehouse_gateway = warehouse_gateway

    async def execute(self, company_id: int) -> List[WarehouseEntity]:
        db_company = await self._company_gateway.get_by_id(company_id)
        if not db_company:
            raise NotFoundException("Company not found")

        return await self._warehouse_gateway.get_by_company(company_id)
