from typing import Protocol

from src.crm.domain.entities.deals import DealEntity, CalculatedCompanyMetrics


class ICreateDealDAO(Protocol):
    async def create(self, deal: DealEntity) -> DealEntity:
        ...


class IUpdateDealDAO(Protocol):
    async def update(self, deal: DealEntity) -> DealEntity:
        ...


class IGetDealDAO(Protocol):
    async def get(self, deal_id: str) -> DealEntity:
        ...


class IDeleteDealDAO(Protocol):
    async def delete(self, deal_id: str) -> None:
        ...


class ICalculatedCompanyMetricsDAO(Protocol):
    async def calculate_company_metrics(self, deal: DealEntity) -> CalculatedCompanyMetrics:
        ...


class IDealsDAO(
    ICreateDealDAO,
    IUpdateDealDAO,
    IGetDealDAO,
    IDeleteDealDAO,
    ICalculatedCompanyMetricsDAO
):
    ...
