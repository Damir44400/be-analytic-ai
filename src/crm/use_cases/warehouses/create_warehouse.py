from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import NotFoundException
from src.crm.domain.entities.warehouse import WarehouseEntity
from src.crm.domain.interfaces.daos.branches import ICompanyBranchGetByUserIdDAO
from src.crm.domain.interfaces.daos.warehouses import IWarehouseCreateDAO
from src.crm.domain.interfaces.daos.warehouses import IWarehouseGetByIdDAO


class WarehouseGateway(
    IWarehouseCreateDAO,
    IWarehouseGetByIdDAO,
):
    ...


class BranchGateway(
    ICompanyBranchGetByUserIdDAO,
):
    ...


class CreateWarehouseUseCase:
    def __init__(
            self,
            uow: IUoW,
            warehouse_gateway: WarehouseGateway,
            branch_gateway: BranchGateway,
    ):
        self._uow = uow
        self._warehouse_gateway = warehouse_gateway
        self._branch_gateway = branch_gateway

    async def execute(self, form: WarehouseEntity, user_id: int):
        db_branch = await self._branch_gateway.get_by_user_id(user_id, form.branch_id)
        if not db_branch:
            raise NotFoundException("Branch not found")
        async with self._uow:
            created = await self._warehouse_gateway.create(form)
            return created
