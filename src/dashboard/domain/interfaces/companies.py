from typing import Protocol, List

from ...domain.entities.companies import CompanyEntity


class ICompanyCreateDAO(Protocol):
    async def create(self, company: CompanyEntity) -> CompanyEntity:
        pass


class ICompanyGetDAO(Protocol):
    async def get_by_id(self, id: int) -> CompanyEntity:
        pass


class ICompanyGetByUserDAO(Protocol):
    async def get_by_user_id(self, user_id: int, company_id: int) -> CompanyEntity:
        pass


class ICompanyUpdateDAO(Protocol):
    async def update(self, company_id: int, company: CompanyEntity) -> CompanyEntity:
        pass


class ICompaniesListByUsersDAO(Protocol):
    async def user_companies(self, user_id: int) -> List[CompanyEntity]:
        pass
