from dataclasses import dataclass
from typing import Optional, List

from src.core.domain.entity import EntityMeta
from .products import ProductEntity


@dataclass(frozen=True)
class CategoryEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    company_id: int = None
    products: List[ProductEntity] = None
