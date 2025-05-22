from dishka import Provider, provide, Scope

from src.core.domain.interfaces import IUoW
from src.crm.domain.interfaces.daos.branches import IBranchesDAO
from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeesDAO
from src.crm.domain.use_cases.branches import (
    IRegisterCompanyBranchUseCase,
    IGetCompanyBranchesUseCase,
    IDeleteCompanyBranchUseCase,
    IUpdateCompanyBranchUseCase
)
from src.crm.use_cases.branches.delete_company_branch import DeleteCompanyBranchUseCase
from src.crm.use_cases.branches.get_company_branches import GetCompanyBranchesUseCase
from src.crm.use_cases.branches.register_company_branch import RegisterCompanyBranchUseCase
from src.crm.use_cases.branches.update_company_branch import UpdateCompanyBranchUseCase


class BranchUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_register_company_branch_use_case(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            company_dao: ICompaniesDAO,
            branch_dao: IBranchesDAO
    ) -> IRegisterCompanyBranchUseCase:
        return RegisterCompanyBranchUseCase(
            uow,
            employee_dao,
            company_dao,
            branch_dao
        )

    @provide(scope=Scope.REQUEST)
    async def get_company_branches_use_case(
            self,
            company_dao: ICompaniesDAO,
            branch_dao: IBranchesDAO
    ) -> IGetCompanyBranchesUseCase:
        return GetCompanyBranchesUseCase(company_dao, branch_dao)

    @provide(scope=Scope.REQUEST)
    async def get_delete_company_branch_use_case(
            self,
            uow: IUoW,
            employee_dao: IEmployeesDAO,
            branch_dao: IBranchesDAO
    ) -> IDeleteCompanyBranchUseCase:
        return DeleteCompanyBranchUseCase(uow, employee_dao, branch_dao)

    @provide(scope=Scope.REQUEST)
    async def get_update_company_branch_use_case(
            self,
            uow: IUoW,
            branch_dao: IBranchesDAO,
            employee_dao: IEmployeesDAO
    ) -> IUpdateCompanyBranchUseCase:
        return UpdateCompanyBranchUseCase(
            uow, branch_dao, employee_dao)
