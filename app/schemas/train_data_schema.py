from pydantic import BaseModel
from typing import Optional


class CompanyMachineBase(BaseModel):
    train_data: str


class CompanyMachineCreate(CompanyMachineBase):
    pass


class CompanyMachineUpdate(CompanyMachineBase):
    pass


class CompanyMachine(CompanyMachineBase):
    id: int
    company_id: int
