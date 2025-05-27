from dishka import Provider, provide, Scope

from src.crm.domain.interfaces.daos.branches import IBranchesDAO
from src.crm.domain.interfaces.daos.categories import ICategoriesDAO
from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeesDAO
from src.crm.domain.interfaces.daos.warehouses import IWarehousesDAO
from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.use_cases.categories import ICategoryCreateUseCase, ICategoryDeleteUseCase, ICategoryUpdateUseCase, \
    ICompanyCategoryListUseCase
from src.crm.domain.use_cases.warehouses import IWarehouseListUseCase
from src.crm.use_cases.branches.get_warehouses import WarehouseListUseCase
from src.crm.use_cases.categories.create_category import CreateCategoryUseCase
from src.crm.use_cases.categories.delete_category import DeleteCategoryUseCase
from src.crm.use_cases.categories.get_categories import GetCategoriesListUseCase
from src.crm.use_cases.categories.update_category import UpdateCategoryUseCase


class CategoryUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_create_categories(
            self,
            uow: IUoW,
            category_dao: ICategoriesDAO,
            employee_dao: IEmployeesDAO,
    ) -> ICategoryCreateUseCase:
        return CreateCategoryUseCase(uow, category_dao, employee_dao)

    @provide(scope=Scope.REQUEST)
    async def get_delete_categories(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            category_dao: ICategoriesDAO
    ) -> ICategoryDeleteUseCase:
        return DeleteCategoryUseCase(uow, category_dao, employee_dao)

    @provide(scope=Scope.REQUEST)
    async def get_update_categories(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            category_dao: ICategoriesDAO
    ) -> ICategoryUpdateUseCase:
        return UpdateCategoryUseCase(uow, category_dao, employee_dao)

    @provide(scope=Scope.REQUEST)
    async def get_list_categories(
            self,
            company_dao: ICompaniesDAO,
            category_dao: ICategoriesDAO
    ) -> ICompanyCategoryListUseCase:
        return GetCategoriesListUseCase(company_gateway=company_dao, category_gateway=category_dao)

    @provide(scope=Scope.REQUEST)
    async def get_warehouse_list_use_case(
            self,
            branch_dao: IBranchesDAO,
            warehouse_dao: IWarehousesDAO
    ) -> IWarehouseListUseCase:
        return WarehouseListUseCase(
            branch_gateway=branch_dao,
            warehouse_gateway=warehouse_dao
        )
