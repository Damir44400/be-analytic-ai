from typing import List

from sqlalchemy import insert, select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.entities.warehouse_transfer import WarehouseTransferEntity
from src.crm.domain.interfaces.daos.warehouse_transfers import IWarehouseTransfersDAO
from src.crm.infrastructure.models.warehouse_transfers import WarehouseTransfer


class WarehouseTransfersDAO(IWarehouseTransfersDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, transfer: WarehouseTransferEntity) -> WarehouseTransferEntity:
        stmt = insert(WarehouseTransfer).values(
            transfer.to_dict(exclude_none=True)
        ).returning(WarehouseTransfer)
        result = await self._session.execute(stmt)
        row = result.scalar_one()
        return WarehouseTransferEntity.to_domain(row)

    async def get_by_id(self, id: int) -> WarehouseTransferEntity:
        stmt = select(WarehouseTransfer).where(WarehouseTransfer.id == id)
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return WarehouseTransferEntity.to_domain(row)

    async def list_by_product(self, product_id: int) -> List[WarehouseTransferEntity]:
        stmt = select(WarehouseTransfer).where(WarehouseTransfer.product_id == product_id)
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [WarehouseTransferEntity.to_domain(r) for r in rows]

    async def list_by_warehouse(self, warehouse_id: int) -> List[WarehouseTransferEntity]:
        stmt = select(WarehouseTransfer).where(
            or_(
                WarehouseTransfer.from_warehouse_id == warehouse_id,
                WarehouseTransfer.to_warehouse_id == warehouse_id
            )
        )
        result = await self._session.execute(stmt)
        rows = result.scalars().all()
        return [WarehouseTransferEntity.to_domain(r) for r in rows]
