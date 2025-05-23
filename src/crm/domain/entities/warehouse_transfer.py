from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.crm.domain.entity import EntityMeta


@dataclass(frozen=True)
class WarehouseTransferEntity(EntityMeta):
    id: Optional[int] = None
    product_id: int = None
    from_warehouse_id: int = None
    to_warehouse_id: int = None
    quantity: int = None
    transfer_date: datetime = None
    comment: Optional[str] = None
