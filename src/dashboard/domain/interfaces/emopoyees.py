from typing import Protocol, List

from src.dashboard.domain.entities.employees import EmployeeEntity


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


class IEmployeeListByCompanyDAO(Protocol):
    async def list_by_company(self, company_id: int) -> List[EmployeeEntity]:
        ...


class IEmployeesDAO(
    IEmployeeCreateDAO,
    IEmployeeUpdateDAO,
    IEmployeeDeleteDAO,
    IEmployeeGetByIdDAO,
    IEmployeeListByCompanyDAO
):
    ...
