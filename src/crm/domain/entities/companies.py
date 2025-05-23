from dataclasses import dataclass
from typing import Optional, List

from src.crm.domain.entity import EntityMeta
from .branches import CompanyBranchEntity
from .products import ProductEntity
from ...infrastructure.models.companies import (
    BusinessTypeEnum
)


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
    branches: Optional[List[CompanyBranchEntity]] = None
    products: Optional[List[ProductEntity]] = None
