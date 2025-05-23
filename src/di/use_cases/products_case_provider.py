from dishka import Provider, provide, Scope

from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO, IEmployeesDAO
from src.crm.domain.interfaces.daos.products import IProductUpdateDAO, IProductDeleteDAO, \
    IProductGetByIdDAO, IProductsDAO
from src.crm.domain.use_cases.products import IProductCreateUseCase, IProductUpdateUseCase, IProductDeleteUseCase, \
    IProductListByCompanyUseCase, IProductListByWarehouseUseCase
from src.crm.use_cases.products.create_products import ProductCreateUseCase
from src.crm.use_cases.products.delete_products import DeleteProductsUseCase
from src.crm.use_cases.products.get_company_products import ListProductsByCompanyUseCase
from src.crm.use_cases.products.get_warehouse_products import ListProductsByWarehouseUseCase
from src.crm.use_cases.products.update_products import UpdateProductUseCase


class ProductUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_create_product(
            self,
            uow: IUoW,
            product_dao: IProductsDAO,
            employee_dao: IEmployeesDAO
    ) -> IProductCreateUseCase:
        return ProductCreateUseCase(uow, product_dao, employee_dao)

    @provide(scope=Scope.REQUEST)
    async def get_update_product(
            self,
            uow: IUoW,
            product_dao: IProductUpdateDAO,
            employee_dao: IEmployeeGetByUserCompanyDAO
    ) -> IProductUpdateUseCase:
        return UpdateProductUseCase(uow, product_dao, employee_dao)

    @provide(scope=Scope.REQUEST)
    async def get_delete_product(
            self,
            uow: IUoW,
            product_dao: IProductDeleteDAO,
            employee_dao: IEmployeeGetByUserCompanyDAO
    ) -> IProductDeleteUseCase:
        return DeleteProductsUseCase(uow, employee_dao, product_dao)

    @provide(scope=Scope.REQUEST)
    async def get_list_by_company(
            self,
            product_dao: IProductGetByIdDAO
    ) -> IProductListByCompanyUseCase:
        return ListProductsByCompanyUseCase(product_dao)

    @provide(scope=Scope.REQUEST)
    async def get_list_by_warehouse(
            self,
            product_dao: IProductGetByIdDAO
    ) -> IProductListByWarehouseUseCase:
        return ListProductsByWarehouseUseCase(product_dao)
