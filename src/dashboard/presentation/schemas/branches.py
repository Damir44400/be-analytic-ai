from typing import Optional

from pydantic import BaseModel, constr


class CompanyBranchForm(BaseModel):
    city: constr(strip_whitespace=True, min_length=1)
    country: constr(strip_whitespace=True, min_length=1)
    address: str


class CompanyBranchCreate(CompanyBranchForm):
    company_id: int


class CompanyBranchUpdate(CompanyBranchForm):
    city: Optional[constr(strip_whitespace=True, min_length=1)] = None
    country: Optional[constr(strip_whitespace=True, min_length=1)] = None
    address: Optional[str] = None


class CompanyBranchRead(BaseModel):
    id: int
    city: str
    country: str
    address: str

    class Config:
        from_attributes = True

class CompanyBranchReadDetailed(CompanyBranchRead):
    ...
    class Config:
        from_attributes = True