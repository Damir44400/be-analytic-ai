from typing import Protocol, List, Optional, Dict

from src.crm.domain.entities.employees import EmployeeEntity


class IEmployeeCreateDAO(Protocol):
    async def create(
            self,
            employee: EmployeeEntity
    ) -> EmployeeEntity:
        ...


class IEmployeeUpdateDAO(Protocol):
    async def update(
            self,
            id: int,
            employee: EmployeeEntity
    ) -> EmployeeEntity:
        ...


class IEmployeeDeleteDAO(Protocol):
    async def delete(
            self,
            id: int
    ) -> None:
        ...


class IEmployeeGetByIdDAO(Protocol):
    async def get_by_id(
            self,
            id: int
    ) -> EmployeeEntity:
        ...


class IEmployeeGetByUserIdDAO(Protocol):
    async def get_by_user_id(
            self,
            user_id: int
    ) -> EmployeeEntity:
        ...


class IEmployeeListByCompanyDAO(Protocol):
    async def list_by_company(self, company_id: int) -> List[EmployeeEntity]:
        ...


class IEmployeeGetByUserCompanyDAO(Protocol):
    async def get_by_user_and_company(self, user_id: int, company_id: int) -> EmployeeEntity:
        ...


class IEmployeeGetByUserBranchDAO(Protocol):
    async def get_by_user_branch(self, user_id: int, branch_id: int) -> EmployeeEntity:
        ...


class IEmployeeGetByUserCategoryDAO(Protocol):
    async def get_by_user_and_category(self, user_id: int, category_id: int) -> EmployeeEntity:
        ...


class IEmployeeFilteredListByCompanyDAO(Protocol):
    async def list_filtered(
            self,
            company_id: int,
            role: Optional[str] = None,
            min_salary: Optional[int] = None,
            max_salary: Optional[int] = None,
            is_manager: Optional[bool] = None,
            status: Optional[str] = None
    ) -> List[EmployeeEntity]:
        ...


class IEmployeeCountByRoleDAO(Protocol):
    async def count_by_role(self, company_id: int) -> Dict[str, int]:
        ...


class IEmployeesDAO(
    IEmployeeCreateDAO,
    IEmployeeUpdateDAO,
    IEmployeeDeleteDAO,
    IEmployeeGetByIdDAO,
    IEmployeeGetByUserIdDAO,
    IEmployeeListByCompanyDAO,
    IEmployeeGetByUserBranchDAO,
    IEmployeeGetByUserCategoryDAO,
    IEmployeeFilteredListByCompanyDAO,
    IEmployeeCountByRoleDAO
):
    ...
