from dataclasses import dataclass
from typing import Protocol, Dict, Optional, List

from src.dashboard.domain.entities.branches import CompanyBranchEntity


@dataclass
class CompanyBranchRegisterForm:
    city: str
    country: str
    postal_code: str
    address: str
    company_id: int


@dataclass
class CompanyBranchUpdateForm:
    city: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    address: Optional[str] = None


class IRegisterCompanyBranchUseCase(Protocol):
    async def execute(self, branch: CompanyBranchRegisterForm, user_id: int) -> CompanyBranchEntity:
        ...


class IGetCompanyBranchesUseCase(Protocol):
    async def execute(self, company_id: int) -> List[CompanyBranchEntity]:
        ...


class IGetCompanyBranchDetailUseCase(Protocol):
    async def execute(self, branch_id: int) -> CompanyBranchEntity:
        ...


class IDeleteCompanyBranchUseCase(Protocol):
    async def execute(self, branch_id: int, user_id: int) -> Dict[str, str]:
        ...


class IUpdateCompanyBranchUseCase(Protocol):
    async def execute(
            self,
            branch_id: int, branch: CompanyBranchUpdateForm,
            user_id: int
    ) -> CompanyBranchEntity:
        ...
