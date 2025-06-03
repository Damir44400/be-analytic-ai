from dataclasses import asdict

from src.crm.domain.entities.branches import CompanyBranchEntity
from src.crm.domain.exceptions import NotFoundException, ForbiddenException
from src.crm.domain.interfaces.daos.branches import (
    ICompanyBranchGetByUserIdDAO,
    ICompanyBranchUpdateDAO,
)
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserBranchDAO
from src.crm.domain.interfaces.uow import IUoW
from src.crm.domain.use_cases.branches import (
    CompanyBranchUpdateForm
)


class Gateway(
    ICompanyBranchUpdateDAO,
    ICompanyBranchGetByUserIdDAO
):
    pass


class UpdateCompanyBranchUseCase:
    def __init__(
            self,
            uow: IUoW,
            dao: Gateway,
            employee_dao: IEmployeeGetByUserBranchDAO,
    ):
        self._uow = uow
        self._dao = dao
        self._employee_dao = employee_dao

    async def execute(
            self,
            branch_id: int,
            form: CompanyBranchUpdateForm,
            user_id: int,
    ) -> CompanyBranchEntity:
        db_employee = await self._employee_dao.get_by_user_branch(
            user_id=user_id,
            branch_id=branch_id
        )
        if not db_employee or not db_employee.is_manager_or_owner:
            raise ForbiddenException("You do not have permission to perform this action.")
        existing = await self._dao.get_by_user_id(user_id, branch_id)
        if not existing:
            raise NotFoundException("Branch not found")

        update_data = CompanyBranchEntity(asdict(form))
        async with self._uow:
            return await self._dao.update(branch_id, update_data)
