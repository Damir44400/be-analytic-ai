from sqlalchemy import insert, select, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.entities.product_category import ProductCategoryEntity
from src.crm.infrastructure.models.product_category import ProductsCategory


class ProductCategoryDAO:
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

    async def get(self, product_id: int, category_id: int) -> ProductCategoryEntity:
        stmt = select(ProductsCategory).where(
            ProductsCategory.product_id == product_id,
            ProductsCategory.category_id == category_id
        )
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return ProductCategoryEntity.to_domain(row)
