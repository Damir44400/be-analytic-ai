import typing
from dataclasses import dataclass
from typing import Optional, List

from src.crm.domain.entity import EntityMeta

if typing.TYPE_CHECKING:
    from .products import ProductEntity


@dataclass(frozen=True)
class WarehouseEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    address: str = None
    branch_id: int = None
    products: List["ProductEntity"] = None
