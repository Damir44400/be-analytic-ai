from typing import Protocol, List

from src.dashboard.domain.entities.branch_employees import BranchEmployeeEntity


class IBranchEmployeeCreateDAO(Protocol):
    async def create(self, employee: BranchEmployeeEntity) -> BranchEmployeeEntity:
        ...


class IBranchEmployeeUpdateDAO(Protocol):
    async def update(self, id: int, employee: BranchEmployeeEntity) -> BranchEmployeeEntity:
        ...


class IBranchEmployeeDeleteDAO(Protocol):
    async def delete(self, id: int) -> None:
        ...


class IBranchEmployeeGetByIdDAO(Protocol):
    async def get_by_id(self, id: int) -> BranchEmployeeEntity:
        ...


class IBranchEmployeeListByBranchIdDAO(Protocol):
    async def list_by_branch_id(self, branch_id: int) -> List[BranchEmployeeEntity]:
        ...


class IBranchEmployeesDAO(
    IBranchEmployeeCreateDAO,
    IBranchEmployeeUpdateDAO,
    IBranchEmployeeDeleteDAO,
    IBranchEmployeeGetByIdDAO,
    IBranchEmployeeListByBranchIdDAO,
):
    ...
