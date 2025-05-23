from dataclasses import dataclass
from typing import Optional

from src.crm.domain.entity import EntityMeta


@dataclass(frozen=True)
class EmployeeEntity(EntityMeta):
    id: Optional[int] = None
    user_id: Optional[int] = None
    company_id: Optional[int] = None
    salary: Optional[float] = None
    status: Optional[str] = None
    role: Optional[str] = None
