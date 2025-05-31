from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import Optional, List


@dataclass
class DealEntity:
    id: Optional[str] = None
    name: Optional[str] = None
    amount: Optional[Decimal] = None
    expected_close_date: Optional[date] = None
    stage: Optional[str] = None
    probability: Optional[float] = None
    lead_id: Optional[int] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    description: Optional[str] = None
    lost_reason: Optional[str] = None


@dataclass
class DealStageMetrics:
    stage_name: str
    count: int = 0
    total_value: Decimal = field(default_factory=lambda: Decimal("0.0"))
    average_value: Decimal = field(default_factory=lambda: Decimal("0.0"))


@dataclass
class CalculatedCompanyMetrics:
    open_deal_metrics_by_stage: List[DealStageMetrics] = field(default_factory=list)
    closed_won_metrics: DealStageMetrics = field(default_factory=lambda: DealStageMetrics(stage_name="Closed Won"))
    closed_lost_metrics: DealStageMetrics = field(default_factory=lambda: DealStageMetrics(stage_name="Closed Lost"))
    total_open_deals_count: int = 0
    total_open_deals_value: Decimal = field(default_factory=lambda: Decimal("0.0"))
    weighted_pipeline_value: Decimal = field(default_factory=lambda: Decimal("0.0"))
    overall_win_rate: Optional[float] = None
    average_deal_value_won: Optional[Decimal] = None
    average_deal_value_lost: Optional[Decimal] = None
    average_sales_cycle_duration_days_won: Optional[float] = None
    average_sales_cycle_duration_days_lost: Optional[float] = None


@dataclass
class AICompanyInsights:
    predicted_revenue_next_period: Optional[Decimal] = None
    predicted_deals_to_close_next_period: Optional[int] = None
    forecast_accuracy_vs_previous: Optional[float] = None
    at_risk_open_deals_count: Optional[int] = None
    at_risk_open_deals_value: Optional[Decimal] = None
    key_factors_driving_wins: List[str] = field(default_factory=list)
    key_factors_leading_to_losses: List[str] = field(default_factory=list)
    common_lost_reasons_summary: List[str] = field(default_factory=list)
    suggested_actions_for_pipeline_improvement: List[str] = field(default_factory=list)
    opportunities_for_growth: List[str] = field(default_factory=list)
    overall_customer_sentiment_trend: Optional[str] = None


@dataclass
class CompanyDealAnalysisReport:
    report_period_description: str
    calculated_metrics: CalculatedCompanyMetrics
    ai_insights: Optional[AICompanyInsights] = None
    deals_summary_list: List[DealEntity] = field(default_factory=list)
    analysis_timestamp: Optional[str] = None
