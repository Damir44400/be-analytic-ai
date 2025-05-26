from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import lazyload

from src.crm.domain.entities.products import ProductEntity
from src.crm.infrastructure.models.products import Product
from src.crm.infrastructure.models.warehouse_products import WarehouseProducts


class ProductsDAO:
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

    async def list_by_company(self, company_id: int, filters: dict) -> List[ProductEntity]:
        stmt = (
            select(Product)
            .where(
                Product.company_id == company_id
            )
            .options(
                lazyload(Product.warehouses),
                lazyload(Product.categories),
            )
        )
        warehouses_id = filters.get("warehouses_id")
        categories_id = filters.get("categories_id")

        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [ProductEntity.to_domain(row) for row in rows]

    async def list_by_warehouse(self, warehouse_id: int) -> List[ProductEntity]:
        stmt = (
            select(Product)
            .join(
                WarehouseProducts,
                WarehouseProducts.warehouse_id == warehouse_id
            )
            .where(WarehouseProducts.warehouse_id == warehouse_id)
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [ProductEntity.to_domain(row) for row in rows]
