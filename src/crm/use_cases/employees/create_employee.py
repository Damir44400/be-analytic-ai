from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException, BadRequestException
from src.crm.domain.entities.employees import EmployeeEntity
from src.crm.domain.interfaces.daos.companies import ICompanyGetDAO
from src.crm.domain.interfaces.daos.emopoyees import (
    IEmployeeCreateDAO,
    IEmployeeGetByUserCompanyDAO
)
from src.crm.infrastructure.models.employees import EmployeeRoleStatusEnum
from src.users.domain.interfaces import IUserGetByIdDAO


class UserGateway(IUserGetByIdDAO):
    ...


class CompanyGateway(
    ICompanyGetDAO
):
    ...


class EmployeeGateway(
    IEmployeeCreateDAO,
    IEmployeeGetByUserCompanyDAO
):
    ...


class CreateEmployeeUseCase:
    def __init__(
            self,
            uow: IUoW,
            user_gateway: UserGateway,
            company_gateway: CompanyGateway,
            employee_gateway: EmployeeGateway
    ):
        self._uow = uow
        self._user_gateway = user_gateway
        self._company_gateway = company_gateway
        self._employee_gateway = employee_gateway

    async def execute(self, form: EmployeeEntity, user_id: int) -> EmployeeEntity:
        db_company = await self._company_gateway.get_by_id(form.company_id)
        if not db_company:
            raise NotFoundException("Company not found")
        db_user = await self._user_gateway.get_user_by_id(form.user_id)
        if not db_user:
            raise NotFoundException("User not found")
        company_owner = await self._employee_gateway.get_by_user_and_company(user_id, form.company_id)
        if not company_owner:
            raise NotFoundException("Employee not found")

        if company_owner.role != EmployeeRoleStatusEnum.OWNER:
            raise BadRequestException("You are not the owner of the company")

        async with self._uow:
            return await self._employee_gateway.create(form)
