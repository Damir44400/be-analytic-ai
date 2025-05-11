from dishka import Provider, provide, Scope

from src.core.domain.interfaces import IUoW
from src.dashboard.domain.interfaces.branches import IBranchesDAO
from src.dashboard.domain.use_cases.branches import (
    IRegisterCompanyBranchUseCase,
    IGetCompanyBranchesUseCase,
    IDeleteCompanyBranchUseCase,
    IUpdateCompanyBranchUseCase
)
from src.dashboard.use_cases.branches.delete_company_branch_use_case import DeleteCompanyBranchUseCase
from src.dashboard.use_cases.branches.get_company_branches_use_case import GetCompanyBranchesUseCase
from src.dashboard.use_cases.branches.register_company_branch_use_case import RegisterCompanyBranchUseCase
from src.dashboard.use_cases.branches.update_company_branch_use_case import UpdateCompanyBranchUseCase


class CompanyBranchUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_register_company_branch_use_case(
            self,
            uow: IUoW,
            branch_dao: IBranchesDAO
    ) -> IRegisterCompanyBranchUseCase:
        return RegisterCompanyBranchUseCase(uow, branch_dao)

    @provide(scope=Scope.REQUEST)
    def get_company_branches_use_case(
            self,
            branch_dao: IBranchesDAO
    ) -> IGetCompanyBranchesUseCase:
        return GetCompanyBranchesUseCase(branch_dao)

    @provide(scope=Scope.REQUEST)
    def get_delete_company_branch_use_case(
            self,
            uow: IUoW,
            branch_dao: IBranchesDAO
    ) -> IDeleteCompanyBranchUseCase:
        return DeleteCompanyBranchUseCase(uow, branch_dao)

    @provide(scope=Scope.REQUEST)
    def get_update_company_branch_use_case(
            self,
            uow: IUoW,
            branch_dao: IBranchesDAO
    ) -> IUpdateCompanyBranchUseCase:
        return UpdateCompanyBranchUseCase(uow, branch_dao)
