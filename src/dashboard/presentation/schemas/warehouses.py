from typing import Optional

from pydantic import BaseModel


class WarehouseCreate(BaseModel):
    name: str
    branch_id: int
    address: str


class WarehouseUpdate(BaseModel):
    name: Optional[str] = None
    branch_id: Optional[int] = None
    address: Optional[str] = None


class WarehouseRead(BaseModel):
    id: int
    name: str
    branch_id: int
    address: str

    class Config:
        orm_mode = True
