from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.exceptions import BadRequestException
from src.crm.domain.entities.categories import CategoryEntity
from src.crm.domain.interfaces.daos.categories import ICategoryCreateDAO, ICategoryGetByNameCompanyDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum


class CategoryGateway(
    ICategoryCreateDAO,
    ICategoryGetByNameCompanyDAO
):
    ...


class CreateCategoryUseCase:
    def __init__(
            self,
            uow: IUoW,
            category_gateway: CategoryGateway,
            employee_gateway: IEmployeeGetByUserCompanyDAO,
    ):
        self._uow = uow
        self._category_gateway = category_gateway
        self._employee_gateway = employee_gateway

    async def execute(self, body: CategoryEntity, user_id: int) -> CategoryEntity:
        db_employee = await self._employee_gateway.get_by_user_and_company(user_id, body.company_id)
        if not db_employee or db_employee.role not in [
            EmployeeRoleStatusEnum.EMPLOYEE.value,
            EmployeeRoleStatusEnum.MANAGER.value
        ]:
            raise BadRequestException("Employee does not have required role or does not exist")
        db_category = await self._category_gateway.get_by_name(body.name, body.company_id)
        if db_category:
            raise BadRequestException("Category already exists with this given name")
        async with self._uow:
            await self._category_gateway.create(body)
        return db_category
