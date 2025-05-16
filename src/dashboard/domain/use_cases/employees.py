from dataclasses import dataclass
from typing import Optional, Protocol, List

from src.dashboard.domain.entities.employees import EmployeeEntity


@dataclass
class EmployeeCreate:
    user_id: int
    company_id: int
    salary: float
    status: str
    role: str


@dataclass
class EmployeeUpdate:
    salary: Optional[float] = None
    status: Optional[str] = None
    role: Optional[str] = None


class IGetEmployeeUseCase(Protocol):
    async def execute(self, company_id: int, employee_id: int) -> Optional[EmployeeEntity]:
        """
        Retrieve a single employee's information by company and employee ID.
        """


class ICreateEmployeeUseCase(Protocol):
    async def execute(self, form: EmployeeCreate) -> Optional[EmployeeEntity]:
        """
        Create a new employee record for a company.
        """


class IUpdateEmployeeUseCase(Protocol):
    async def execute(
            self,
            employee_id: int,
            form: EmployeeUpdate
    ) -> Optional[EmployeeEntity]:
        """
        Update employee details such as salary, status, and role.
        """


class IDeleteEmployeeUseCase(Protocol):
    async def execute(self, employee_id: int) -> None:
        """
        Delete an employee's record from the system.
        """


class IListEmployeesUseCase(Protocol):
    async def execute(self, company_id: int) -> List[EmployeeEntity]:
        """
        List all employees in a specific company.
        """
