from dataclasses import dataclass
from typing import Optional, List

from src.core.domain.entity import EntityMeta
from .employees import BranchEmployeeEntity
from .warehouse import WarehouseEntity


@dataclass(frozen=True)
class CompanyBranchEntity(EntityMeta):
    id: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    company_id: Optional[int] = None
    warehouses: List[WarehouseEntity] = None
    employees: List[BranchEmployeeEntity] = None
