from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.branches import CompanyBranchEntity
from src.dashboard.domain.interfaces.branches import IBranchesDAO
from src.dashboard.infrastructure.models.branches import CompanyBranch
from src.dashboard.infrastructure.models.companies import Company


class BranchesDAO(IBranchesDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, branch: CompanyBranchEntity) -> CompanyBranchEntity:
        stmt = insert(CompanyBranch).values(branch.to_dict(exclude_none=True)).returning(CompanyBranch)
        result = await self._session.execute(stmt)
        branch_row = result.scalar_one()
        return CompanyBranchEntity.to_domain(branch_row)

    async def get_by_id(self, id: int) -> CompanyBranchEntity:
        stmt = select(CompanyBranch).where(CompanyBranch.id == id)
        result = await self._session.execute(stmt)
        branch = result.scalar_one_or_none()
        return CompanyBranchEntity.to_domain(branch)

    async def get_by_company_id(self, company_id: int) -> List[CompanyBranchEntity]:
        stmt = (
            select(CompanyBranch)
            .where(CompanyBranch.company_id == company_id)
            .options(CompanyBranch.warehouses)
        )
        result = await self._session.execute(stmt)
        branches = result.scalars().all()
        return [CompanyBranchEntity.to_domain(branch) for branch in branches]

    async def update(self, branch_id: int, branch: CompanyBranchEntity) -> CompanyBranchEntity:
        stmt = (
            update(CompanyBranch)
            .where(CompanyBranch.id == branch_id)
            .values(branch.to_dict(exclude_none=True))
            .returning(CompanyBranch)
        )
        result = await self._session.execute(stmt)
        updated = result.scalar_one()
        return CompanyBranchEntity.to_domain(updated)

    async def delete(self, branch_id: int) -> None:
        stmt = delete(CompanyBranch).where(CompanyBranch.id == branch_id)
        await self._session.execute(stmt)

    async def get_by_user_id(self, user_id: int, branch_id: int) -> CompanyBranchEntity:
        stmt = (
            select(CompanyBranch)
            .join(Company, Company.id == CompanyBranch.company_id)
            .where(Company.user_id == user_id, CompanyBranch.id == branch_id)
        )
        result = await self._session.execute(stmt)
        branch = result.scalar_one_or_none()
        return CompanyBranchEntity.to_domain(branch)
