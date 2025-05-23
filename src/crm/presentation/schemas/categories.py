from typing import Optional

from pydantic import BaseModel


class CompanyCategoryRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CompanyCategoryCreate(BaseModel):
    name: str
    company_id: int

    class Config:
        from_attributes = True


class CompanyCategoryUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        from_attributes = True
