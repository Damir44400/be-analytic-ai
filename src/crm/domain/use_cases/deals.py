from typing import Protocol, Dict, Tuple, List

from src.crm.domain.entities.deals import DealEntity, CalculatedCompanyMetrics


class IDealsCreateUseCase(Protocol):
    async def execute(self, deal: DealEntity) -> DealEntity:
        ...


class IDealsUpdateUseCase(Protocol):
    async def execute(self, deal_id: int, deal: DealEntity) -> DealEntity:
        ...


class IDealsDeleteUseCase(Protocol):
    async def execute(self, deal_id: int) -> Dict[str, str]:
        ...


class IGetDealUseCase(Protocol):
    async def execute(self, deal_id: int) -> DealEntity:
        ...


class ICompanyDealsWithMetricsUseCase(Protocol):
    async def execute(self, company_id: int) -> Tuple[List[DealEntity], CalculatedCompanyMetrics]:
        ...
