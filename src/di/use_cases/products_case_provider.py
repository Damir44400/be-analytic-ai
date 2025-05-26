from dishka import Provider, provide, Scope

from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO, IEmployeesDAO
from src.crm.domain.interfaces.daos.products import IProductsDAO
from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.use_cases.products import IProductCreateUseCase, IProductUpdateUseCase, IProductDeleteUseCase
from src.crm.use_cases.products.create_products import ProductCreateUseCase
from src.crm.use_cases.products.delete_products import DeleteProductsUseCase
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
            product_dao: IProductsDAO,
            employee_dao: IEmployeeGetByUserCompanyDAO
    ) -> IProductUpdateUseCase:
        return UpdateProductUseCase(uow, product_dao, employee_dao)

    @provide(scope=Scope.REQUEST)
    async def get_delete_product(
            self,
            uow: IUoW,
            product_dao: IProductsDAO,
            employee_dao: IEmployeeGetByUserCompanyDAO
    ) -> IProductDeleteUseCase:
        return DeleteProductsUseCase(uow, employee_dao, product_dao)
