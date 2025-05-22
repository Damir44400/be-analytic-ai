from typing import Protocol, List

from src.crm.domain.entities.companies import CompanyEntity


class ICompanyCreateDAO(Protocol):
    async def create(
            self,
            company: CompanyEntity
    ) -> CompanyEntity:
        ...


class ICompanyGetDAO(Protocol):
    async def get_by_id(
            self,
            company_id: int
    ) -> CompanyEntity:
        ...


class ICompanyGetByUserIdDAO(Protocol):
    async def get_by_user_id(
            self,
            user_id: int,
            company_id: int
    ) -> CompanyEntity:
        ...


class ICompanyUpdateDAO(Protocol):
    async def update(
            self,
            company_id: int,
            company: CompanyEntity
    ) -> CompanyEntity:
        ...


class ICompaniesListByUsersDAO(Protocol):
    async def user_companies(self, user_id: int) -> List[CompanyEntity]:
        ...


class ICompanyDeleteDAO(Protocol):
    async def delete(
            self,
            company_id: int
    ) -> CompanyEntity:
        ...


class ICompaniesDAO(
    ICompanyGetDAO,
    ICompanyCreateDAO,
    ICompanyGetByUserIdDAO,
    ICompanyUpdateDAO,
    ICompaniesListByUsersDAO,
    ICompanyDeleteDAO,
):
    ...
