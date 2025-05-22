from typing import Optional, List

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


class CompanyBranchReadWarehouses(CompanyBranchRead):
    warehouses: List[dict]

    class Config:
        from_attributes = True


class CompanyBranchReadEmployees(CompanyBranchRead):
    employees: List[dict]

    class Config:
        from_attributes = True