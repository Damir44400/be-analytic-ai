from dishka import Provider, provide, Scope

from src.crm.domain.interfaces.daos.branches import IBranchesDAO
from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.products import IProductsDAO
from src.crm.domain.interfaces.daos.warehouses import (
    IWarehousesDAO,
)
from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.use_cases.warehouses import (
    IWarehouseCreateUseCase,
    IWarehouseUpdateUseCase,
    IWarehouseDeleteUseCase,
    ICompanyWarehouseUseCase, IGetWarehouseProductsUseCase,
)
from src.crm.use_cases.warehouses.create_warehouse import CreateWarehouseUseCase
from src.crm.use_cases.warehouses.delete_warehouse import DeleteWarehouseUseCase
from src.crm.use_cases.warehouses.get_company_warehouses import CompanyWarehousesListUseCase
from src.crm.use_cases.warehouses.get_warehouse_products import GetWarehouseProductsUseCase
from src.crm.use_cases.warehouses.update_warehouse import UpdateWarehouseUseCase


class WarehouseUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_warehouse_create_use_case(
            self,
            uow: IUoW,
            warehouse_dao: IWarehousesDAO,
            branch_dao: IBranchesDAO
    ) -> IWarehouseCreateUseCase:
        return CreateWarehouseUseCase(uow, warehouse_dao, branch_dao)

    @provide(scope=Scope.REQUEST)
    async def get_warehouse_update_use_case(
            self,
            uow: IUoW,
            warehouse_dao: IWarehousesDAO
    ) -> IWarehouseUpdateUseCase:
        return UpdateWarehouseUseCase(uow, warehouse_dao)

    @provide(scope=Scope.REQUEST)
    async def get_warehouse_delete_use_case(
            self,
            uow: IUoW,
            warehouse_dao: IWarehousesDAO
    ) -> IWarehouseDeleteUseCase:
        return DeleteWarehouseUseCase(uow, warehouse_dao)

    @provide(scope=Scope.REQUEST)
    async def get_company_warehouse_use_case(
            self,
            company_dao: ICompaniesDAO,
            warehouse_dao: IWarehousesDAO
    ) -> ICompanyWarehouseUseCase:
        return CompanyWarehousesListUseCase(
            company_gateway=company_dao,
            warehouse_gateway=warehouse_dao
        )

    @provide(scope=Scope.REQUEST)
    async def get_warehouse_products_use_case(
            self,
            warehouse_dao: IWarehousesDAO,
            products_dao: IProductsDAO
    ) -> IGetWarehouseProductsUseCase:
        return GetWarehouseProductsUseCase(
            warehouse_dao=warehouse_dao,
            products_dao=products_dao
        )
