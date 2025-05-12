from dataclasses import dataclass
from typing import Optional, List

from src.core.domain.entity import EntityMeta
from ...infrastructure.models.companies import (
    BusinessActivityEnum,
    BusinessTypeEnum
)
from ...infrastructure.models.branches import CompanyBranch


@dataclass(frozen=True)
class CompanyEntity(EntityMeta):
    id: Optional[int] = None
    company_logo: Optional[str] = None
    company_name: Optional[str] = None
    business_type: Optional[BusinessTypeEnum] = None
    description: Optional[str] = None
    company_website: Optional[str] = None
    company_phone_number: Optional[str] = None
    user_id: Optional[int] = None
    branches: Optional[List[CompanyBranch]] = None