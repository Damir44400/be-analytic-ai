from dataclasses import dataclass
from typing import Optional, List

from src.core.domain.entity import EntityMeta
from .products import ProductEntity


@dataclass(frozen=True)
class WarehouseEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    address: str = None
    branch_id: int = None
    products: List[ProductEntity] = None
