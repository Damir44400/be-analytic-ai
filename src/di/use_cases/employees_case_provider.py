from dishka import Provider, provide, Scope

from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeesDAO
from src.crm.domain.interfaces.daos.users import IUserDAO
from src.crm.domain.interfaces.uow import IUoW
from src.crm.use_cases.employees.create_employee import CreateEmployeeUseCase


class EmployeesCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_create_employee_use_case(
            self,
            uow: IUoW,
            user_dao: IUserDAO,
            company_dao: ICompaniesDAO,
            employee_dao: IEmployeesDAO,
    ):
        return CreateEmployeeUseCase(
            uow,
            user_dao,
            company_dao,
            employee_dao
        )
