from typing import Optional, List

from pydantic import BaseModel

from .user import BaseUserProfile


class EmployeeBase(BaseModel):
    salary: int
    status: str
    role: str
    is_owner: bool
    is_manager: bool


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    salary: Optional[int] = None
    status: Optional[str] = None
    role: Optional[str] = None
    is_owner: Optional[bool] = None
    is_manager: Optional[bool] = None


class EmployeeRead(EmployeeBase):
    id: int
    user: BaseUserProfile


class CompanyEmployee(BaseModel):
    employees: List[EmployeeRead]
    all_role_counts: dict
    outed_role_counts: dict
