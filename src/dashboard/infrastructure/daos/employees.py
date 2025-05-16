from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.employees import EmployeeEntity
from src.dashboard.infrastructure.models.employees import Employee


class EmployeesDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, employee: EmployeeEntity) -> EmployeeEntity:
        stmt = insert(Employee).values(employee.to_dict(exclude_none=True)).returning(Employee)
        result = await self._session.execute(stmt)
        employee = result.scalars().first()
        return EmployeeEntity.to_domain(employee)

    async def get_by_id(self, id: int) -> EmployeeEntity:
        stmt = select(Employee).where(Employee.id == id)
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.to_domain(employee) if employee else None

    async def get_by_user_and_company(self, user_id: int, company_id: int) -> EmployeeEntity:
        stmt = select(Employee).where(
            Employee.user_id == user_id,
            Employee.company_id == company_id
        )
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.to_domain(employee) if employee else None

    async def list_by_company(self, company_id: int) -> List[EmployeeEntity]:
        stmt = select(Employee).where(Employee.company_id == company_id)
        result = await self._session.execute(stmt)
        employees = result.scalars().all()
        return [EmployeeEntity.to_domain(e) for e in employees]

    async def update(self, employee_id: int, employee: EmployeeEntity) -> EmployeeEntity:
        stmt = (
            update(Employee)
            .where(Employee.id == employee_id)
            .values(
                employee.to_dict(
                    exclude_none=True
                )
            )
            .returning(Employee)
        )
        result = await self._session.execute(stmt)
        employee = result.scalars().first()
        return EmployeeEntity.to_domain(employee)

    async def delete(self, employee_id: int) -> None:
        stmt = delete(Employee).where(Employee.id == employee_id)
        await self._session.execute(stmt)
