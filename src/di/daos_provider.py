from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.interfaces.daos.branches import IBranchesDAO
from src.crm.domain.interfaces.daos.categories import ICategoriesDAO
from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeesDAO
from src.crm.domain.interfaces.daos.product_category import IProductCategoryDAO
from src.crm.domain.interfaces.daos.products import IProductsDAO
from src.crm.domain.interfaces.daos.users import IUserDAO
from src.crm.domain.interfaces.daos.warehouse_products import IWarehouseProductDAO
from src.crm.domain.interfaces.daos.warehouses import IWarehousesDAO
from src.crm.infrastructure.daos.branches import BranchesDAO
from src.crm.infrastructure.daos.categories import CategoriesDAO
from src.crm.infrastructure.daos.companies import CompaniesDAO
from src.crm.infrastructure.daos.employees import EmployeesDAO
from src.crm.infrastructure.daos.product_category import ProductCategoryDAO
from src.crm.infrastructure.daos.products import ProductsDAO
from src.crm.infrastructure.daos.user_dao import UserDAO
from src.crm.infrastructure.daos.warehouse_products import WarehouseProductDAO
from src.crm.infrastructure.daos.warehouses import WarehousesDAO


class DashboardDaosProviders(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_companies_dao(self, session: AsyncSession) -> ICompaniesDAO:
        return CompaniesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_company_branches_dao(self, session: AsyncSession) -> IBranchesDAO:
        return BranchesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_warehouses_dao(self, session: AsyncSession) -> IWarehousesDAO:
        return WarehousesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_user_dao(self, session: AsyncSession) -> IUserDAO:
        return UserDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_employees_dao(self, session: AsyncSession) -> IEmployeesDAO:
        return EmployeesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_products_dao(self, session: AsyncSession) -> IProductsDAO:
        return ProductsDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_categories_dao(self, session: AsyncSession) -> ICategoriesDAO:
        return CategoriesDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_warehouse_products_dao(self, session: AsyncSession) -> IWarehouseProductDAO:
        return WarehouseProductDAO(session)

    @provide(scope=Scope.REQUEST)
    async def get_category_products_dao(self, session: AsyncSession) -> IProductCategoryDAO:
        return ProductCategoryDAO(session)
