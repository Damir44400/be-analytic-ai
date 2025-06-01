from typing import Protocol, List

from src.crm.domain.entities.deals import DealEntity, CalculatedCompanyMetrics


class ICreateDealDAO(Protocol):
    async def create(self, deal: DealEntity) -> DealEntity:
        ...


class IUpdateDealDAO(Protocol):
    async def update(self, deal_id: int, deal: DealEntity) -> DealEntity:
        ...


class IGetDealDAO(Protocol):
    async def get(self, deal_id: int) -> DealEntity:
        ...


class IDeleteDealDAO(Protocol):
    async def delete(self, deal_id: int) -> None:
        ...


class ICalculatedCompanyMetricsDAO(Protocol):
    async def calculate_company_metrics(self, company_id: int) -> CalculatedCompanyMetrics:
        ...


class ICompanyDealsDAO(Protocol):
    async def company_deals(self, company_id: int) -> List[DealEntity]:
        ...


class IDealsDAO(
    ICreateDealDAO,
    IUpdateDealDAO,
    IGetDealDAO,
    IDeleteDealDAO,
    ICalculatedCompanyMetricsDAO
):
    ...
