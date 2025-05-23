from typing import Optional, List

from pydantic import BaseModel

from src.crm.presentation.schemas.warehouses import WarehouseRead


class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    company_id: int
    warehouse_id: Optional[List[int]] = None

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    warehouse_id: Optional[List[int]] = None

    class Config:
        from_attributes = True


class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None
    company_id: int
    warehouses: List[WarehouseRead]

    class Config:
        from_attributes = True
