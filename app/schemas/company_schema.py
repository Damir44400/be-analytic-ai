from pydantic import BaseModel
from typing import Optional


class CompanyBase(BaseModel):
    title: str
    description: Optional[str] = None
    type_company: str


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
