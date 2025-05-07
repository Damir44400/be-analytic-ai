from typing import List

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.dashboard.domain.entities.companies import CompanyEntity
from src.dashboard.domain.interfaces.companies import (
    ICompanyGetDAO,
    ICompanyCreateDAO,
    ICompanyGetByUserDAO,
    ICompanyUpdateDAO,
    ICompaniesListByUsersDAO
)
from src.dashboard.infrastructure.models.companies import Company


class ICompaniesDAO(
    ICompanyGetDAO,
    ICompanyCreateDAO,
    ICompanyGetByUserDAO,
    ICompanyUpdateDAO,
    ICompaniesListByUsersDAO
):
    pass


class CompaniesDAO(ICompaniesDAO):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, company: CompanyEntity) -> CompanyEntity:
        stmt = insert(Company).values(company.to_dict(exclude_none=True))
        company = await self._session.execute(stmt)
        return CompanyEntity.to_domain(company)

    async def get_by_id(self, id: int) -> Company:
        stmt = select(Company).where(Company.id == id)
        company = await self._session.execute(stmt)
        company = company.scalar_one_or_none()
        return CompanyEntity.to_domain(company)

    async def get_by_user_id(self, user_id: int, company_id: int) -> Company:
        stmt = select(Company).where(Company.id == company_id, Company.user_id == user_id)
        company = await self._session.execute(stmt)
        company = company.scalar_one_or_none()
        return CompanyEntity.to_domain(company)

    async def user_companies(self, user_id: int) -> List[CompanyEntity]:
        stmt = select(Company).where(Company.user_id == user_id)
        companies = await self._session.execute(stmt)
        companies = companies.scalars().all()
        return [CompanyEntity.to_domain(company) for company in companies]

    async def update(self, company_id: int, company: CompanyEntity) -> CompanyEntity:
        stmt = update(Company).where(Company.id == company_id).values(company.to_dict(exclude_none=True))
        company = await self._session.execute(stmt)
        return CompanyEntity.to_domain(company)
