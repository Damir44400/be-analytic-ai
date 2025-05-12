from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class ProductEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    quantity: int = None
    type: str = None
    price: float = None
