from typing import List

from src.crm.domain.entities.product_category import ProductCategoryEntity
from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.entities.warehouse_product import WarehouseProductEntity
from src.crm.domain.exceptions import ForbiddenException
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.interfaces.daos.product_category import IProductCategoryAddDAO
from src.crm.domain.interfaces.daos.products import IProductCreateDAO
from src.crm.domain.interfaces.daos.warehouse_products import (
    IWarehouseProductAddDAO
)
from src.crm.domain.interfaces.uow import IUoW


class WarehouseProductGateway(
    IWarehouseProductAddDAO,
):
    ...


class CategoryProductGateway(
    IProductCategoryAddDAO,
):
    ...


class ProductCreateUseCase:
    def __init__(
            self,
            uow: IUoW,
            product_dao: IProductCreateDAO,
            employee_dao: IEmployeeGetByUserCompanyDAO,
            product_warehouse_dao: WarehouseProductGateway,
            product_category_dao: CategoryProductGateway
    ):
        self._uow = uow
        self._product_dao = product_dao
        self._employee_dao = employee_dao
        self._product_warehouse_dao = product_warehouse_dao
        self._product_category_dao = product_category_dao

    async def execute(self, form: ProductEntity, user_id: int) -> ProductEntity:
        db_employee = await self._employee_dao.get_by_user_and_company(user_id=user_id, company_id=form.company_id)

        if db_employee is None or not db_employee.is_manager_or_owner:
            raise ForbiddenException("User does not have the necessary permissions to create a product.")
        categories_id: List[int] = form.categories_id
        warehouses_id: List[int] = form.warehouses_id
        async with self._uow:
            product = await self._product_dao.create(form.exclude(["categories_id", "warehouses_id"]))

            for warehouse_id in warehouses_id:
                await self._product_warehouse_dao.add(
                    WarehouseProductEntity(
                        product_id=product.id,
                        warehouse_id=warehouse_id,
                    )
                )

            for category_id in categories_id:
                await self._product_category_dao.add(
                    ProductCategoryEntity(
                        product_id=product.id,
                        category_id=category_id,
                    )
                )
        return product
