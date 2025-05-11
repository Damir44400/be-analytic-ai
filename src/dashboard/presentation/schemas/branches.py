from typing import Optional

from pydantic import BaseModel, constr


class CompanyBranchForm(BaseModel):
    city: constr(strip_whitespace=True, min_length=1)
    country: constr(strip_whitespace=True, min_length=1)
    postal_code: Optional[str]
    address: str


class CompanyBranchRead(BaseModel):
    id: int
    city: str
    country: str
    postal_code: Optional[str]
    address: str

    class Config:
        from_attributes = True
