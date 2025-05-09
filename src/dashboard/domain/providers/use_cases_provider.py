from dishka import Provider, provide, Scope

from src.core.domain.interfaces import IUoW
from src.dashboard.domain.interfaces.companies import ICompaniesDAO
from src.dashboard.domain.interfaces.company_branches import IBranchesDAO
from src.dashboard.domain.use_cases.companies import IGetUserCompaniesUseCase, IUpdateCompanyUseCase
from src.dashboard.domain.use_cases.companies import IRegisterCompanyUseCase
from src.dashboard.use_cases.companies.get_user_companies_use_case import (
    GetUserCompaniesUseCase
)
from src.dashboard.use_cases.companies.register_company_use_case import (
    RegisterCompanyUseCase
)
from src.dashboard.use_cases.companies.update_company_use_case import UpdateCompanyUseCase


class DashboardUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_register_company_use_case(
            self,
            uow: IUoW,
            company_dao: ICompaniesDAO,
            company_branch_dao: IBranchesDAO
    ) -> IRegisterCompanyUseCase:
        return RegisterCompanyUseCase(uow, company_dao, company_branch_dao)

    @provide(scope=Scope.REQUEST)
    def get_user_companies_use_case(
            self,
            company_dao: ICompaniesDAO,
    ) -> IGetUserCompaniesUseCase:
        return GetUserCompaniesUseCase(company_dao)

    @provide(scope=Scope.REQUEST)
    def get_company_update_use_case(
            self,
            uow: IUoW,
            company_dao: ICompaniesDAO) -> IUpdateCompanyUseCase:
        return UpdateCompanyUseCase(uow, company_dao)
