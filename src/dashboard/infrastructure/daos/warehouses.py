from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.warehouse import WarehouseEntity
from src.dashboard.infrastructure.models.branches import CompanyBranch
from src.dashboard.infrastructure.models.companies import Company
from src.dashboard.infrastructure.models.employees import Employee
from src.dashboard.infrastructure.models.warehouse import Warehouse


class WarehousesDAO:
    def __init__(
            self,
            session: AsyncSession
    ):
        self._session = session

    async def create(self, warehouse: WarehouseEntity) -> WarehouseEntity:
        stmt = insert(Warehouse).values(warehouse.to_dict(exclude_none=True)).returning(Warehouse)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return WarehouseEntity.to_domain(row)

    async def update(self, id: int, warehouse: WarehouseEntity) -> WarehouseEntity:
        stmt = (
            update(Warehouse)
            .where(Warehouse.id == id)
            .values(warehouse.to_dict(exclude_none=True))
            .returning(Warehouse)
        )
        result = await self._session.execute(stmt)
        updated = result.scalar_one()
        return WarehouseEntity.to_domain(updated)

    async def delete(self, id: int) -> None:
        stmt = delete(Warehouse).where(Warehouse.id == id)
        await self._session.execute(stmt)

    async def get_by_id(self, id: int) -> WarehouseEntity:
        stmt = select(Warehouse).where(Warehouse.id == id)
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return WarehouseEntity.to_domain(row)

    async def list_by_branch_id(self, branch_id: int) -> List[WarehouseEntity]:
        stmt = select(Warehouse).where(Warehouse.branch_id == branch_id)
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [WarehouseEntity.to_domain(r) for r in rows]

    async def get_by_company(self, company_id: int) -> List[WarehouseEntity]:
        stmt = (
            select(Warehouse)
            .join(CompanyBranch, CompanyBranch.company_id == company_id)
            .where(Warehouse.branch_id == CompanyBranch.id)
            .distinct(Warehouse.name, Warehouse.branch_id)
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [WarehouseEntity.to_domain(r) for r in rows]

    async def get_by_user(self, id: int, user_id: int) -> WarehouseEntity | None:
        stmt = (
            select(Warehouse)
            .join(CompanyBranch, CompanyBranch.id == Warehouse.branch_id)
            .join(Company, Company.id == CompanyBranch.company_id)
            .join(Employee, Employee.company_id == Company.id)
            .where(
                Warehouse.id == id,
                Employee.user_id == user_id
            )
        )
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return WarehouseEntity.to_domain(row)
