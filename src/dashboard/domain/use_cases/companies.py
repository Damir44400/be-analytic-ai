from dataclasses import dataclass
from typing import Protocol, Dict, Optional, List

from src.dashboard.domain.entities.companies import CompanyEntity
from src.dashboard.domain.use_cases.company_branches import CompanyBranchForm
from src.dashboard.infrastructure.models.companies import BusinessTypeEnum, BusinessActivityEnum


@dataclass
class CompanyRegisterForm:
    company_name: str
    business_type: BusinessTypeEnum
    business_activity: BusinessActivityEnum
    description: str
    company_website: Optional[str] = None
    company_phone_number: Optional[str] = None
    company_logo: Optional[bytes] = None
    branches: List[CompanyBranchForm] = None


@dataclass
class CompanyUpdateForm:
    company_name: Optional[str] = None
    business_type: Optional[BusinessTypeEnum] = None
    business_activity: Optional[BusinessActivityEnum] = None
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
    async def execute(self, company_id: int, user_id: int) -> CompanyEntity: ...


class IDeleteCompanyUseCase(Protocol):
    async def execute(self, company_id: int, user_id: int) -> Dict[str, str]: ...


class IUpdateCompanyUseCase(Protocol):
    async def execute(
            self, company_id: int, company: CompanyUpdateForm, user_id: int
    ) -> CompanyEntity: ...
