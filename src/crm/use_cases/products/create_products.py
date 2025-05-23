from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import BadRequestException
from src.crm.domain.entities.products import ProductEntity
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.interfaces.daos.products import IProductCreateDAO
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class ProductCreateUseCase:
    def __init__(
            self,
            uow: IUoW,
            product_dao: IProductCreateDAO,
            employee_dao: IEmployeeGetByUserCompanyDAO,
    ):
        self._uow = uow
        self._product_dao = product_dao
        self._employee_dao = employee_dao

    async def execute(self, form: ProductEntity, user_id: int) -> ProductEntity:
        db_employee = await self._employee_dao.get_by_user_and_company(user_id=user_id, company_id=form.company_id)

        if db_employee is None or db_employee.role == EmployeeRoleStatusEnum.EMPLOYEE:
            raise BadRequestException("User does not have the necessary permissions to create a product.")

        async with self._uow:
            product = await self._product_dao.create(form)
        return product
