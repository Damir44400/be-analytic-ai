from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.branch_employees import BranchEmployeeEntity
from src.dashboard.domain.interfaces.branch_employees import IBranchEmployeesDAO
from src.dashboard.infrastructure.models.branch_employees import BranchEmployees


class BranchEmployeesDAO(IBranchEmployeesDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, employee: BranchEmployeeEntity) -> BranchEmployeeEntity:
        stmt = insert(BranchEmployees).values(employee.to_dict(exclude_none=True)).returning(BranchEmployees)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return BranchEmployeeEntity.to_domain(row)

    async def update(self, id: int, employee: BranchEmployeeEntity) -> BranchEmployeeEntity:
        stmt = (
            update(BranchEmployees)
            .where(BranchEmployees.id == id)
            .values(employee.to_dict(exclude_none=True))
            .returning(BranchEmployees)
        )
        result = await self._session.execute(stmt)
        updated = result.scalar_one()
        return BranchEmployeeEntity.to_domain(updated)

    async def delete(self, id: int) -> None:
        stmt = delete(BranchEmployees).where(BranchEmployees.id == id)
        await self._session.execute(stmt)

    async def get_by_id(self, id: int) -> BranchEmployeeEntity:
        stmt = select(BranchEmployees).where(BranchEmployees.id == id)
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return BranchEmployeeEntity.to_domain(row)

    async def list_by_branch_id(self, branch_id: int) -> List[BranchEmployeeEntity]:
        stmt = select(BranchEmployees).where(BranchEmployees.branch_id == branch_id)
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [BranchEmployeeEntity.to_domain(emp) for emp in rows]
