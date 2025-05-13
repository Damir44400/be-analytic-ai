from typing import List

from sqlalchemy import insert, select, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.warehouse_product import WarehouseProductEntity
from src.dashboard.domain.interfaces.warehouse_products import IWarehouseProductDAO
from src.dashboard.infrastructure.models.warehouse_products import WarehouseProducts


class WarehouseProductDAO(IWarehouseProductDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, relation: WarehouseProductEntity) -> WarehouseProductEntity:
        stmt = insert(WarehouseProducts).values(
            relation.to_dict(exclude_none=True)
        ).returning(WarehouseProducts)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return WarehouseProductEntity.to_domain(row)

    async def delete(self, product_id: int, warehouse_id: int) -> None:
        stmt = delete(WarehouseProducts).where(
            and_(
                WarehouseProducts.product_id == product_id,
                WarehouseProducts.warehouse_id == warehouse_id
            )
        )
        await self._session.execute(stmt)

    async def list_by_product_id(self, product_id: int) -> List[WarehouseProductEntity]:
        stmt = select(WarehouseProducts).where(
            WarehouseProducts.product_id == product_id
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [WarehouseProductEntity.to_domain(r) for r in rows]

    async def list_by_warehouse_id(self, warehouse_id: int) -> List[WarehouseProductEntity]:
        stmt = select(WarehouseProducts).where(
            WarehouseProducts.warehouse_id == warehouse_id
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [WarehouseProductEntity.to_domain(r) for r in rows]
