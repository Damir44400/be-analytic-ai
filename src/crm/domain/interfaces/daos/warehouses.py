from typing import Protocol, List

from src.crm.domain.entities.warehouse import WarehouseEntity


class IWarehouseCreateDAO(Protocol):
    async def create(self, warehouse: WarehouseEntity) -> WarehouseEntity:
        ...


class IWarehouseUpdateDAO(Protocol):
    async def update(self, id: int, warehouse: WarehouseEntity) -> WarehouseEntity:
        ...


class IWarehouseDeleteDAO(Protocol):
    async def delete(self, id: int) -> None:
        ...


class IWarehouseGetByIdDAO(Protocol):
    async def get_by_id(self, id: int) -> WarehouseEntity:
        ...


class IWarehouseGetByUserDAO(Protocol):
    async def get_by_user(self, id: int, user_id: int) -> WarehouseEntity:
        ...


class IWarehouseListByBranchDAO(Protocol):
    async def list_by_branch_id(self, branch_id: int) -> List[WarehouseEntity]:
        ...


class IWarehousesGetByCompany(Protocol):
    async def get_by_company(self, company_id: int) -> List[WarehouseEntity]:
        ...


class IWarehousesDAO(
    IWarehouseCreateDAO,
    IWarehouseUpdateDAO,
    IWarehouseDeleteDAO,
    IWarehouseGetByIdDAO,
    IWarehouseListByBranchDAO,
    IWarehousesGetByCompany,
    IWarehouseGetByUserDAO
):
    ...
