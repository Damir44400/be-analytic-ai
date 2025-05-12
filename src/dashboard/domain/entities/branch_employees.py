from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class BranchEmployeeEntity(EntityMeta):
    id: Optional[int] = None
    user_id: Optional[int] = None
    branch_id: Optional[int] = None
    salary: float = None
    status: str = None
