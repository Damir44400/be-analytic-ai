from dataclasses import dataclass
from datetime import date
from typing import Optional

from src.crm.domain.entity import EntityMeta
from src.crm.infrastructure.models.deals import DealStage


@dataclass
class DealEntity(EntityMeta):
    name: Optional[str] = None
    amount: Optional[float] = None
    expected_close_date: Optional[date] = None
    stage: Optional[DealStage] = None
    probability: Optional[float] = None
    lead_id: Optional[int] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    description: Optional[str] = None
    lost_reason: Optional[str] = None
