from dataclasses import dataclass
from typing import Optional, List

from src.crm.domain.entity import EntityMeta
from .employees import EmployeeEntity
from .warehouse import WarehouseEntity


@dataclass(frozen=True)
class CompanyBranchEntity(EntityMeta):
    id: Optional[int] = None
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    company_id: Optional[int] = None
    warehouses: List[WarehouseEntity] = None
    employees: List[EmployeeEntity] = None
