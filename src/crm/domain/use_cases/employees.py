from typing import Optional, Protocol, List

from src.crm.domain.entities.employees import EmployeeEntity


class IGetEmployeeUseCase(Protocol):
    async def execute(self, company_id: int, employee_id: int) -> Optional[EmployeeEntity]:
        """
        Retrieve a single employee's information by company and employee ID.
        """


class ICreateEmployeeUseCase(Protocol):
    async def execute(self, form: EmployeeEntity) -> Optional[EmployeeEntity]:
        """
        Create a new employee record for a company.
        """


class IUpdateEmployeeUseCase(Protocol):
    async def execute(
            self,
            employee_id: int,
            form: EmployeeEntity
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
