from datetime import timezone
from decimal import Decimal
from typing import Dict, List

from sqlalchemy import (
    insert,
    select,
    update,
    delete
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.entities.deals import (
    DealEntity,
    CalculatedCompanyMetrics,
    DealStageMetrics
)
from src.crm.infrastructure.models.deals import Deal, DealStage


class DealsDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, deal: DealEntity) -> DealEntity:
        stmt = insert(Deal).values(deal.to_dict(exclude_none=True))
        result = await self._session.execute(stmt)
        deal = result.scalar()
        return DealEntity.from_domain(deal)

    async def get(self, deal_id: int) -> DealEntity:
        stmt = select(Deal).where(Deal.id == deal_id)
        result = await self._session.execute(stmt)
        deal = result.scalar_one_or_none()
        return DealEntity.from_domain(deal)

    async def update(self, deal_id: int, deal: DealEntity) -> DealEntity:
        stmt = update(Deal).values(deal.to_dict(exclude_none=True)).where(Deal.id == deal_id)
        result = await self._session.execute(stmt)
        deal = result.scalar_one_or_none()
        return DealEntity.from_domain(deal)

    async def delete(self, deal_id: int) -> None:
        stmt = delete(Deal).where(Deal.id == deal_id)
        result = await self._session.execute(stmt)
        deleted = result.scalars()
        return len(deleted) > 0

    async def calculate_company_metrics(self, company_id: int) -> CalculatedCompanyMetrics:
        stmt = select(Deal).where(Deal.company_id == company_id)
        result = await self._session.execute(stmt)
        deals_iterable = result.scalars()

        metrics = CalculatedCompanyMetrics()
        open_stages_data: Dict[str, DealStageMetrics] = {}

        total_sales_cycle_duration_won_seconds: float = 0.0
        total_sales_cycle_duration_lost_seconds: float = 0.0

        async for deal in deals_iterable:
            deal_amount = Decimal(str(deal.amount)) if deal.amount is not None else Decimal("0.0")

            created_at_aware = deal.created_at
            if created_at_aware.tzinfo is None:
                created_at_aware = created_at_aware.replace(tzinfo=timezone.utc)

            updated_at_aware = deal.updated_at
            if updated_at_aware.tzinfo is None:
                updated_at_aware = updated_at_aware.replace(tzinfo=timezone.utc)

            if deal.stage == DealStage.CLOSED_WON:
                metrics.closed_won_metrics.deal_count += 1
                metrics.closed_won_metrics.total_value += deal_amount
                duration = updated_at_aware - created_at_aware
                total_sales_cycle_duration_won_seconds += duration.total_seconds()

            elif deal.stage == DealStage.CLOSED_LOST:
                metrics.closed_lost_metrics.deal_count += 1
                metrics.closed_lost_metrics.total_value += deal_amount
                duration = updated_at_aware - created_at_aware
                total_sales_cycle_duration_lost_seconds += duration.total_seconds()

            else:
                metrics.total_open_deals_count += 1
                metrics.total_open_deals_value += deal_amount

                if deal.amount is not None:
                    metrics.weighted_pipeline_value += Decimal(str(deal.amount * deal.probability))

                stage_name_str = deal.stage.value
                if stage_name_str not in open_stages_data:
                    open_stages_data[stage_name_str] = DealStageMetrics(stage_name=stage_name_str)

                open_stages_data[stage_name_str].deal_count += 1
                open_stages_data[stage_name_str].total_value += deal_amount

        metrics.open_deal_metrics_by_stage = sorted(
            list(open_stages_data.values()),
            key=lambda x: x.stage_name
        )

        total_closed_deals_count = metrics.closed_won_metrics.deal_count + metrics.closed_lost_metrics.deal_count
        if total_closed_deals_count > 0:
            metrics.overall_win_rate = (metrics.closed_won_metrics.deal_count / total_closed_deals_count) * 100.0

        if metrics.closed_won_metrics.deal_count > 0:
            metrics.average_deal_value_won = metrics.closed_won_metrics.total_value / Decimal(
                metrics.closed_won_metrics.deal_count)
            metrics.average_sales_cycle_duration_days_won = total_sales_cycle_duration_won_seconds / metrics.closed_won_metrics.deal_count / (
                    24 * 60 * 60)

        if metrics.closed_lost_metrics.deal_count > 0:
            metrics.average_deal_value_lost = metrics.closed_lost_metrics.total_value / Decimal(
                metrics.closed_lost_metrics.deal_count)
            metrics.average_sales_cycle_duration_days_lost = (
                    total_sales_cycle_duration_lost_seconds
                    / metrics.closed_lost_metrics.deal_count / (
                            24 * 60 * 60
                    )
            )

        return metrics

    async def company_deals(self, company_id: int) -> List[DealEntity]:
        stmt = select(Deal).where(Deal.company_id == company_id)
        result = await self._session.execute(stmt)
        deals = result.scalars().all()
        return [DealEntity.from_domain(deal) for deal in deals]
