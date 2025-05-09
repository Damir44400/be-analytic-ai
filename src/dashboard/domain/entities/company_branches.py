from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass(frozen=True)
class CompanyBranchEntity(EntityMeta):
    id: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    address: Optional[str] = None
    company_id: Optional[int] = None
