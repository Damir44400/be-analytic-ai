from typing import List

from sqlalchemy import insert, select, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.product_category import ProductCategoryEntity
from src.dashboard.domain.interfaces.product_category import IProductCategoryDAO
from src.dashboard.infrastructure.models.product_category import ProductsCategory


class ProductCategoryDAO(IProductCategoryDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, relation: ProductCategoryEntity) -> ProductCategoryEntity:
        stmt = insert(ProductsCategory).values(
            relation.to_dict(exclude_none=True)
        ).returning(ProductsCategory)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return ProductCategoryEntity.to_domain(row)

    async def delete(self, product_id: int, category_id: int) -> None:
        stmt = delete(ProductsCategory).where(
            and_(
                ProductsCategory.product_id == product_id,
                ProductsCategory.category_id == category_id
            )
        )
        await self._session.execute(stmt)

    async def list_by_product_id(self, product_id: int) -> List[ProductCategoryEntity]:
        stmt = select(ProductsCategory).where(
            ProductsCategory.product_id == product_id
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [ProductCategoryEntity.to_domain(r) for r in rows]

    async def list_by_category_id(self, category_id: int) -> List[ProductCategoryEntity]:
        stmt = select(ProductsCategory).where(
            ProductsCategory.category_id == category_id
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [ProductCategoryEntity.to_domain(r) for r in rows]
