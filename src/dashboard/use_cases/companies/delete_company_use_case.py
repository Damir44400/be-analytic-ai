from typing import Dict

from src.core.domain.interfaces import IUoW
from src.core.exceptions import NotFoundException
from src.dashboard.domain.interfaces.companies import ICompanyDeleteDAO, ICompanyGetByUserIdDAO
from src.dashboard.domain.use_cases.companies import IDeleteCompanyUseCase


class Gateway(ICompanyDeleteDAO, ICompanyGetByUserIdDAO):
    pass


class DeleteCompanyUseCase(IDeleteCompanyUseCase):
    def __init__(
            self,
            uow: IUoW,
            company_dao: Gateway,
    ):
        self._uow = uow
        self._company_dao = company_dao

    async def execute(self, company_id: int, user_id: int) -> Dict[str, str]:
        db_company = await self._company_dao.get_by_user_id(user_id=user_id, company_id=company_id)
        if not db_company:
            raise NotFoundException("Company not found")

        async with self._uow:
            await self._company_dao.delete(company_id=company_id)
        return {"detail": "Company deleted"}
