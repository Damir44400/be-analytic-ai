import typing
from dataclasses import dataclass
from typing import Optional, List

from src.crm.domain.entity import EntityMeta

if typing.TYPE_CHECKING:
    from src.crm.domain.entities.warehouse import WarehouseEntity
    from src.crm.domain.entities.categories import CategoryEntity


@dataclass(frozen=True)
class ProductEntity(EntityMeta):
    id: Optional[int] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    type: Optional[str] = None
    price: Optional[float] = None
    warehouses_id: Optional[List[int]] = None
    categories_id: Optional[List[int]] = None
    company_id: Optional[int] = None
    categories: Optional[List["CategoryEntity"]] = None
    warehouses: Optional[List["WarehouseEntity"]] = None
