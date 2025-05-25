from typing import Optional, List

from fastapi import Query
from pydantic import BaseModel, Field

from src.crm.presentation.schemas.categories import CompanyCategoryRead
from src.crm.presentation.schemas.warehouses import WarehouseRead


class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    company_id: int
    warehouse_id: Optional[List[int]] = None
    warehouses_id: Optional[List[int]] = None
    categories_id: Optional[List[int]] = None

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    warehouse_id: Optional[List[int]] = None
    warehouses_id: Optional[List[int]] = None
    categories_id: Optional[List[int]] = None

    class Config:
        from_attributes = True


class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None
    company_id: int
    warehouses: List[WarehouseRead]
    categories: List[CompanyCategoryRead]

    class Config:
        from_attributes = True


class ProductFilter():
    model_config = {"extra": "forbid"}

    name: str = Field(Query())
    price: float = Field(Query())
    description: str = Field(Query())
    company_id: int = Field(Query())
    warehouses_id: List[int] = Field(Query([]))
    categories_id: List[int] = Field(Query([]))
