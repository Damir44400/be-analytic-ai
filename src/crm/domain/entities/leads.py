from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.crm.domain.entity import EntityMeta
from src.crm.infrastructure.models.leads import LeadStatus


@dataclass
class LeadEntity(EntityMeta):
    id: Optional[int] = None
    name: str = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    source: Optional[str] = None
    status: Optional[LeadStatus] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    product_id: Optional[int] = None
    comments: Optional[str] = None
