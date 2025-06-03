from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.entities.employees import EmployeeEntity
from src.crm.infrastructure.models.branches import CompanyBranch
from src.crm.infrastructure.models.categories import Category
from src.crm.infrastructure.models.employees import Employee


class EmployeesDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, employee: EmployeeEntity) -> EmployeeEntity:
        stmt = insert(Employee).values(employee.to_dict(exclude_none=True)).returning(Employee)
        result = await self._session.execute(stmt)
        employee = result.scalars().first()
        return EmployeeEntity.from_domain(employee)

    async def get_by_id(self, id: int) -> EmployeeEntity:
        stmt = select(Employee).where(Employee.id == id)
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.from_domain(employee) if employee else None

    async def get_by_user_and_company(self, user_id: int, company_id: int) -> EmployeeEntity:
        stmt = select(Employee).where(
            Employee.user_id == user_id,
            Employee.company_id == company_id
        )
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.from_domain(employee) if employee else None

    async def list_by_company(self, company_id: int) -> List[EmployeeEntity]:
        stmt = select(Employee).where(Employee.company_id == company_id)
        result = await self._session.execute(stmt)
        employees = result.scalars().all()
        return [EmployeeEntity.from_domain(e) for e in employees]

    async def update(self, employee_id: int, data: EmployeeEntity) -> EmployeeEntity:
        stmt = (
            update(Employee)
            .where(Employee.id == employee_id)
            .values(
                data.to_dict(
                    exclude_none=True
                )
            )
            .returning(Employee)
        )
        result = await self._session.execute(stmt)
        employee = result.scalars().first()
        return EmployeeEntity.from_domain(employee)

    async def delete(self, employee_id: int) -> None:
        stmt = delete(Employee).where(Employee.id == employee_id)
        await self._session.execute(stmt)

    async def get_by_user_id(self, user_id: int) -> EmployeeEntity:
        stmt = select(Employee).where(Employee.user_id == user_id)
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.from_domain(employee) if employee else None

    async def get_by_user_branch(self, user_id: int, branch_id: int) -> EmployeeEntity:
        stmt = (
            select(Employee)
            .join(
                CompanyBranch,
                CompanyBranch.company_id == Employee.company_id
            )
            .where(
                CompanyBranch.id == branch_id,
                Employee.user_id == user_id
            )
        )
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.from_domain(employee) if employee else None

    async def get_by_user_and_category(self, user_id: int, category_id: int) -> EmployeeEntity:
        stmt = (
            select(Employee)
            .join(
                Category,
                Category.company_id == Employee.company_id
            )
            .where(
                Category.id == category_id,
                Employee.user_id == user_id
            )
        )
        result = await self._session.execute(stmt)
        employee = result.scalar_one_or_none()
        return EmployeeEntity.from_domain(employee) if employee else None
