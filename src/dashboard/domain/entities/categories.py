from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class CategoryEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    company_id: int = None
