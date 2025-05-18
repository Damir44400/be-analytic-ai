from dishka import Provider, provide, Scope

from src.core.domain.interfaces import IUoW
from src.dashboard.domain.interfaces.branches import IBranchesDAO
from src.dashboard.domain.interfaces.companies import ICompaniesDAO
from src.dashboard.domain.use_cases.companies import (
    IGetUserCompaniesUseCase,
    IUpdateCompanyUseCase,
    IGetCompanyDetailUseCase,
    IDeleteCompanyUseCase
)
from src.dashboard.domain.use_cases.companies import IRegisterCompanyUseCase
from src.dashboard.use_cases.companies.delete_company import DeleteCompanyUseCase
from src.dashboard.use_cases.companies.get_detailed_companies import GetDetailedCompaniesUseCase
from src.dashboard.use_cases.companies.get_user_companies import (
    GetUserCompaniesUseCase
)
from src.dashboard.use_cases.companies.register_company import (
    RegisterCompanyUseCase
)
from src.dashboard.use_cases.companies.update_company import UpdateCompanyUseCase


class CompanyUseCasesProvider(Provider):
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

    @provide(scope=Scope.REQUEST)
    def get_company_detailed_use_case(
            self,
            company_dao: ICompaniesDAO
    ) -> IGetCompanyDetailUseCase:
        return GetDetailedCompaniesUseCase(company_dao)

    @provide(scope=Scope.REQUEST)
    def update_company_detailed_use_case(
            self,
            uow: IUoW,
            company_dao: ICompaniesDAO,
    ) -> IUpdateCompanyUseCase:
        return UpdateCompanyUseCase(uow, company_dao)

    @provide(scope=Scope.REQUEST)
    def delete_company_detailed_use_case(
            self,
            uow: IUoW,
            company_dao: ICompaniesDAO
    ) -> IDeleteCompanyUseCase:
        return DeleteCompanyUseCase(uow, company_dao)
