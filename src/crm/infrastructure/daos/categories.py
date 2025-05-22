from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.entities.categories import CategoryEntity
from src.crm.infrastructure.models.categories import Category


class CategoriesDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, category: CategoryEntity) -> CategoryEntity:
        stmt = insert(Category).values(category.to_dict(exclude_none=True)).returning(Category)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return CategoryEntity.to_domain(row)

    async def update(self, id: int, category: CategoryEntity) -> CategoryEntity:
        stmt = (
            update(Category)
            .where(Category.id == id)
            .values(category.to_dict(exclude_none=True))
            .returning(Category)
        )
        result = await self._session.execute(stmt)
        updated = result.scalar_one()
        return CategoryEntity.to_domain(updated)

    async def delete(self, id: int) -> None:
        stmt = delete(Category).where(Category.id == id)
        await self._session.execute(stmt)

    async def get_by_id(self, id: int) -> CategoryEntity:
        stmt = select(Category).where(Category.id == id)
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return CategoryEntity.to_domain(row)

    async def list_by_company_id(self, company_id: int) -> List[CategoryEntity]:
        stmt = select(Category).where(Category.company_id == company_id)
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [CategoryEntity.to_domain(cat) for cat in rows]
