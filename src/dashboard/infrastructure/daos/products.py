from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.products import ProductEntity
from src.dashboard.domain.interfaces.products import IProductsDAO
from src.dashboard.infrastructure.models.products import Product


class ProductsDAO(IProductsDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, product: ProductEntity) -> ProductEntity:
        stmt = insert(Product).values(product.to_dict(exclude_none=True)).returning(Product)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return ProductEntity.to_domain(row)

    async def update(self, id: int, product: ProductEntity) -> ProductEntity:
        stmt = (
            update(Product)
            .where(Product.id == id)
            .values(product.to_dict(exclude_none=True))
            .returning(Product)
        )
        result = await self._session.execute(stmt)
        updated = result.scalar_one()
        return ProductEntity.to_domain(updated)

    async def delete(self, id: int) -> None:
        stmt = delete(Product).where(Product.id == id)
        await self._session.execute(stmt)

    async def get_by_id(self, id: int) -> ProductEntity:
        stmt = select(Product).where(Product.id == id)
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return ProductEntity.to_domain(row)

    async def list_all(self) -> List[ProductEntity]:
        stmt = select(Product)
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [ProductEntity.to_domain(row) for row in rows]
