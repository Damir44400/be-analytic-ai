from dataclasses import dataclass
from typing import Optional, Protocol, List

from src.dashboard.domain.entities.branch_employees import BranchEmployeeEntity


@dataclass
class BranchEmployeesCreate:
    user_id: int
    branch_id: Optional[int]
    salary: float
    status: str


@dataclass
class BranchEmployeesUpdate:
    branch_id: Optional[int] = None
    salary: Optional[float] = None
    status: Optional[str] = None


class IGetBranchEmployeesUseCase(Protocol):
    async def execute(self, branch_id: int, employee_id: int) -> Optional[BranchEmployeeEntity]:
        ...


class ICreateBranchEmployeesUseCase(Protocol):
    async def execute(self, form: BranchEmployeesCreate) -> Optional[BranchEmployeeEntity]:
        ...


class IUpdateBranchEmployeesUseCase(Protocol):
    async def execute(
            self,
            employee_id: int,
            form: BranchEmployeesUpdate
    ) -> Optional[BranchEmployeeEntity]:
        ...


class IDeleteBranchEmployeesUseCase(Protocol):
    async def execute(self, employee_id: int) -> None:
        ...


class IListBranchEmployeesUseCase(Protocol):
    async def execute(self, branch_id: int) -> List[BranchEmployeeEntity]:
        ...
