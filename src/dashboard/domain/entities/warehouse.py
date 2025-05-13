from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class WarehouseEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    address: str = None
    branch_id: int = None
