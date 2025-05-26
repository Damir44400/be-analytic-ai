from typing import Optional, List

from pydantic import BaseModel, HttpUrl, constr

from src.crm.infrastructure.models.companies import BusinessTypeEnum
from .branches import CompanyBranchForm


class CompanyBase(BaseModel):
    company_name: constr(strip_whitespace=True, min_length=1)
    business_type: BusinessTypeEnum
    description: str
    company_website: Optional[HttpUrl] = None
    company_phone_number: Optional[str] = None


class CompanyCreate(CompanyBase):
    company_logo: Optional[bytes] = None
    branches: Optional[List[CompanyBranchForm]] = None


class CompanyUpdate(CompanyBase):
    company_name: Optional[constr(strip_whitespace=True, min_length=1)] = None
    business_type: BusinessTypeEnum = None
    description: str = None
    company_website: Optional[HttpUrl] = None
    company_phone_number: Optional[str] = None
    company_logo: Optional[bytes] = None


class CompanyRead(CompanyBase):
    id: int
    company_logo: Optional[str] = None

    class Config:
        from_attributes = True


class UserCompaniesRead(BaseModel):
    id: int
    company_name: str

    class Config:
        from_attributes = True
