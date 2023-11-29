from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: Optional[str]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: Optional[int]

    class Config:
        from_attributes = True
