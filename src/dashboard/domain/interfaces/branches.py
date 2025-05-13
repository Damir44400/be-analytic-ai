from typing import Protocol, List

from ..entities.warehouse import WarehouseEntity
from ...domain.entities.branches import CompanyBranchEntity


class ICompanyBranchCreateDAO(Protocol):
    async def create(self, branch: CompanyBranchEntity) -> CompanyBranchEntity:
        ...


class ICompanyBranchGetDAO(Protocol):
    async def get_by_id(self, id: int) -> CompanyBranchEntity:
        ...


class ICompanyBranchGetByCompanyDAO(Protocol):
    async def get_by_company_id(self, company_id: int) -> List[CompanyBranchEntity]:
        ...


class ICompanyBranchUpdateDAO(Protocol):
    async def update(
            self,
            branch_id: int,
            branch: CompanyBranchEntity
    ) -> CompanyBranchEntity:
        ...


class ICompanyBranchDeleteDAO(Protocol):
    async def delete(self, branch_id: int) -> None:
        ...


class ICompanyBranchGetByUserIdDAO(Protocol):
    async def get_by_user_id(self, user_id: int, branch_id: int) -> CompanyBranchEntity:
        ...


class ICompanyBranchWarehousesDAO(Protocol):
    async def get_warehouses(self, branch_id: int) -> CompanyBranchEntity:
        ...


class IBranchesDAO(
    ICompanyBranchCreateDAO,
    ICompanyBranchGetDAO,
    ICompanyBranchGetByCompanyDAO,
    ICompanyBranchUpdateDAO,
    ICompanyBranchDeleteDAO,
    ICompanyBranchGetByUserIdDAO,
    ICompanyBranchWarehousesDAO
):
    ...
