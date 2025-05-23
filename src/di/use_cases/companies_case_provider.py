from dishka import Provider, provide, Scope

from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.interfaces.daos.branches import IBranchesDAO
from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeesDAO
from src.crm.domain.use_cases.companies import (
    IGetUserCompaniesUseCase,
    IUpdateCompanyUseCase,
    IGetCompanyDetailUseCase,
    IDeleteCompanyUseCase
)
from src.crm.domain.use_cases.companies import IRegisterCompanyUseCase
from src.crm.use_cases.companies.delete_company import DeleteCompanyUseCase
from src.crm.use_cases.companies.get_detailed_companies import GetDetailedCompaniesUseCase
from src.crm.use_cases.companies.get_user_companies import (
    GetUserCompaniesUseCase
)
from src.crm.use_cases.companies.register_company import (
    RegisterCompanyUseCase
)
from src.crm.use_cases.companies.update_company import UpdateCompanyUseCase


class CompanyUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_register_company_use_case(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            company_dao: ICompaniesDAO,
            company_branch_dao: IBranchesDAO
    ) -> IRegisterCompanyUseCase:
        return RegisterCompanyUseCase(uow, employee_dao, company_dao, company_branch_dao)

    @provide(scope=Scope.REQUEST)
    async def get_user_companies_use_case(
            self,
            company_dao: ICompaniesDAO,
    ) -> IGetUserCompaniesUseCase:
        return GetUserCompaniesUseCase(company_dao)

    @provide(scope=Scope.REQUEST)
    async def get_company_update_use_case(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            company_dao: ICompaniesDAO
    ) -> IUpdateCompanyUseCase:
        return UpdateCompanyUseCase(uow, employee_dao, company_dao)

    @provide(scope=Scope.REQUEST)
    async def get_company_detailed_use_case(
            self,
            company_dao: ICompaniesDAO
    ) -> IGetCompanyDetailUseCase:
        return GetDetailedCompaniesUseCase(company_dao)

    @provide(scope=Scope.REQUEST)
    async def update_company_detailed_use_case(
            self,
            uow: IUoW,
            company_dao: ICompaniesDAO,
    ) -> IUpdateCompanyUseCase:
        return UpdateCompanyUseCase(uow, company_dao)

    @provide(scope=Scope.REQUEST)
    async def delete_company_detailed_use_case(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            company_dao: ICompaniesDAO
    ) -> IDeleteCompanyUseCase:
        return DeleteCompanyUseCase(uow, employee_dao, company_dao)
