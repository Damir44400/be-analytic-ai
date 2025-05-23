from dataclasses import dataclass
from typing import Optional

from src.crm.domain.entity import EntityMeta


@dataclass(frozen=True)
class ProductEntity(EntityMeta):
    id: Optional[int] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    type: Optional[str] = None
    price: Optional[float] = None
    company_id: Optional[int] = None
