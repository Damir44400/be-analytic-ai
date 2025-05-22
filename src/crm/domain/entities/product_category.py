from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class ProductCategoryEntity(EntityMeta):
    id: Optional[int] = None
    product_id: int = None
    category_id: int = None
