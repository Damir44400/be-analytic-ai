from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Optional, List, Dict

from src.crm.infrastructure.models.leads import LeadStatus


@dataclass
class LeadEntity:
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    source: Optional[str] = None
    status: Optional[LeadStatus] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    product_id: Optional[int] = None
    comments: Optional[str] = None


@dataclass
class LeadSourceMetrics:
    source_name: str
    total_leads: int = 0
    qualified_leads: int = 0
    converted_to_deal_leads: int = 0
    qualification_rate: Optional[float] = None
    conversion_to_deal_rate: Optional[float] = None


@dataclass
class LeadStatusMetrics:
    status_name: LeadStatus
    count: int = 0
    average_age_in_status_days: Optional[float] = None


@dataclass
class LeadFunnelStage:
    stage_name: str
    count_at_stage_start: int
    count_at_stage_end: int
    conversion_rate_to_next: Optional[float]
    average_time_in_stage_days: Optional[float] = None


@dataclass
class CalculatedLeadMetrics:
    total_leads_generated_period: int = 0
    new_leads_this_period: int = 0

    leads_by_source_metrics: List[LeadSourceMetrics] = field(default_factory=list)
    leads_by_current_status_metrics: List[LeadStatusMetrics] = field(default_factory=list)

    lead_funnel_analysis: List[LeadFunnelStage] = field(default_factory=list)

    overall_qualification_rate: Optional[float] = None
    overall_conversion_to_deal_rate: Optional[float] = None

    average_lead_age_days: Optional[float] = None
    average_time_to_qualification_days: Optional[float] = None
    average_time_to_conversion_days: Optional[float] = None

    disqualification_reasons_summary: Dict[str, int] = field(default_factory=dict)
    product_interest_summary: Dict[str, int] = field(default_factory=dict)


@dataclass
class AILeadInsights:
    predicted_lead_score_distribution: Dict[str, int] = field(default_factory=dict)
    predicted_conversion_likelihood_average: Optional[float] = None

    at_risk_leads_count: Optional[int] = None
    at_risk_leads_value_potential: Optional[Decimal] = None

    key_factors_for_successful_qualification: List[str] = field(default_factory=list)
    key_factors_for_disqualification: List[str] = field(default_factory=list)

    predicted_best_performing_sources_next_period: List[str] = field(default_factory=list)
    predicted_underperforming_sources_next_period: List[str] = field(default_factory=list)

    suggested_optimal_follow_up_cadence: Optional[str] = None
    common_objections_and_responses: Dict[str, str] = field(default_factory=dict)

    forecasted_qualified_leads_next_period: Optional[int] = None
    forecasted_conversions_to_deal_next_period: Optional[int] = None


@dataclass
class LeadAnalysisReport:
    report_period_description: str

    calculated_metrics: CalculatedLeadMetrics
    analysis_timestamp: datetime = field(default_factory=datetime.now)
    ai_insights: Optional[AILeadInsights] = None

    top_priority_leads: List[LeadEntity] = field(default_factory=list)
    stale_leads_needing_attention: List[LeadEntity] = field(default_factory=list)

    executive_summary: Optional[str] = None
