from typing import Protocol, List

from ...domain.entities.company_branches import CompanyBranchEntity


class ICompanyBranchCreateDAO(Protocol):
    async def create(self, branch: CompanyBranchEntity) -> CompanyBranchEntity:
        pass


class ICompanyBranchGetDAO(Protocol):
    async def get_by_id(self, id: int) -> CompanyBranchEntity:
        pass


class ICompanyBranchGetByCompanyDAO(Protocol):
    async def get_by_company_id(self, company_id: int) -> List[CompanyBranchEntity]:
        pass


class ICompanyBranchUpdateDAO(Protocol):
    async def update(self, branch_id: int, branch: CompanyBranchEntity) -> CompanyBranchEntity:
        pass


class ICompanyBranchDeleteDAO(Protocol):
    async def delete(self, branch_id: int) -> None:
        pass


class IBranchesDAO(
    ICompanyBranchCreateDAO,
    ICompanyBranchGetDAO,
    ICompanyBranchGetByCompanyDAO,
    ICompanyBranchUpdateDAO,
    ICompanyBranchDeleteDAO
):
    ...
