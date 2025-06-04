from dataclasses import dataclass
from typing import Protocol, Dict, Optional, List, Any

from src.crm.domain.entities.companies import CompanyEntity
from src.crm.infrastructure.models.companies import BusinessTypeEnum
from src.crm.presentation.schemas.branches import CompanyBranchForm


@dataclass
class CompanyRegisterForm:
    company_name: str
    business_type: BusinessTypeEnum
    description: str
    company_website: Optional[str] = None
    company_phone_number: Optional[str] = None
    company_logo: Optional[bytes] = None
    branches: List[CompanyBranchForm] = None


@dataclass
class CompanyUpdateForm:
    company_name: Optional[str] = None
    business_type: Optional[BusinessTypeEnum] = None
    description: Optional[str] = None
    company_website: Optional[str] = None
    company_phone_number: Optional[str] = None
    company_logo: Optional[bytes] = None


class IRegisterCompanyUseCase(Protocol):
    async def execute(self, company: CompanyRegisterForm, user_id: int) -> Dict[str, str]:
        ...


class IGetUserCompaniesUseCase(Protocol):
    async def execute(self, user_id: int) -> List[CompanyEntity]:
        ...


class IGetCompanyDetailUseCase(Protocol):
    async def execute(self, company_id: int) -> CompanyEntity: ...


class IDeleteCompanyUseCase(Protocol):
    async def execute(self, company_id: int, user_id: int) -> Dict[str, str]: ...


class IUpdateCompanyUseCase(Protocol):
    async def execute(
            self, company_id: int, company: CompanyUpdateForm, user_id: int
    ) -> CompanyEntity: ...


class IGetCompanyEmployees(Protocol):
    async def execute(
            self,
            company_id: int,
            role: Optional[str] = None,
            min_salary: Optional[int] = None,
            max_salary: Optional[int] = None,
            is_manager: Optional[bool] = None,
            status: Optional[str] = None
    ) -> Dict[str, Any]:
        ...
