from src.crm.domain.exceptions import BadRequestException, ForbiddenException
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.interfaces.daos.products import IProductDeleteDAO, IProductGetByIdDAO
from src.crm.domain.interfaces.uow import IUoW


class ProductGateway(
    IProductDeleteDAO,
    IProductGetByIdDAO
):
    ...


class DeleteProductsUseCase:
    def __init__(
            self,
            uow: IUoW,
            employee_dao: IEmployeeGetByUserCompanyDAO,
            product_dao: ProductGateway
    ):
        self._uow = uow
        self._employee_dao = employee_dao
        self._product_dao = product_dao

    async def execute(self, user_id: int, product_id: int, company_id: int):
        db_employee = await self._employee_dao.get_by_user_and_company(
            user_id=user_id,
            company_id=company_id
        )
        if db_employee is None or not db_employee.is_owner:
            raise ForbiddenException("User does not have the necessary permissions to delete the product.")

        product = await self._product_dao.get_by_id(product_id)
        if product is None:
            raise BadRequestException("Product not found.")

        async with self._uow:
            await self._product_dao.delete(product_id)

        return {"message": "Product deleted successfully"}
