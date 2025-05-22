from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class WarehouseProductEntity(EntityMeta):
    id: Optional[int] = None
    product_id: int = None
    warehouse_id: int = None
