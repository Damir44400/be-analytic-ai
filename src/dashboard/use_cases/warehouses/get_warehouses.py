from typing import List

from src.core.exceptions import NotFoundException
from src.dashboard.domain.entities.warehouse import WarehouseEntity
from src.dashboard.domain.interfaces.daos.branches import ICompanyBranchGetByUserIdDAO
from src.dashboard.domain.interfaces.daos.warehouses import IWarehouseListByBranchDAO


class BranchGateway(ICompanyBranchGetByUserIdDAO):
    pass


class WarehouseGateway(IWarehouseListByBranchDAO):
    pass


class WarehouseListUseCase:
    def __init__(
            self,
            branch_gateway: BranchGateway,
            warehouse_gateway: WarehouseGateway
    ):
        self._branch_gateway = branch_gateway
        self._warehouse_gateway = warehouse_gateway

    async def execute(self, branch_id: int, user_id: int) -> List[WarehouseEntity]:
        db_branch = await self._branch_gateway.get_by_user_id(user_id=user_id, branch_id=branch_id)
        if not db_branch:
            raise NotFoundException("Branch not found")

        return await self._warehouse_gateway.list_by_branch_id(db_branch.id)
