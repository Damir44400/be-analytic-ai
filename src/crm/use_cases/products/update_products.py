from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import BadRequestException, NotFoundException
from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.interfaces.daos.products import IProductUpdateDAO, IProductGetByIdDAO
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class ProductGateway(
    IProductUpdateDAO,
    IProductGetByIdDAO
):
    ...


class UpdateProductUseCase:
    def __init__(
            self,
            uow: IUoW,
            product_dao: ProductGateway,
            employee_dao: IEmployeeGetByUserCompanyDAO
    ):
        self._uow = uow
        self._product_dao = product_dao
        self._employee_dao = employee_dao

    async def execute(
            self,
            user_id: int,
            company_id: int,
            product_id: int,
            product_data: ProductEntity
    ) -> ProductEntity:
        db_employee = await self._employee_dao.get_by_user_and_company(user_id=user_id, company_id=company_id)
        if db_employee is None or db_employee.role == EmployeeRoleStatusEnum.EMPLOYEE:
            raise BadRequestException("User does not have the necessary permissions to update the product.")

        product = await self._product_dao.get_by_id(product_id)
        if product is None:
            raise NotFoundException("Product not found.")
        async with self._uow:
            updated_product = await self._product_dao.update(product_id, product_data)

        return updated_product
