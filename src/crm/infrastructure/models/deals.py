import enum

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.dialects import postgresql

from src.crm.infrastructure.database.database import Base

class DealStage(enum.Enum):
    QUALIFICATION = "Qualification"
    NEEDS_ANALYSIS = "Needs Analysis"
    PROPOSAL_SENT = "Proposal Sent"
    NEGOTIATION = "Negotiation"
    CLOSED_WON = "Closed Won"
    CLOSED_LOST = "Closed Lost"


class Deal(Base):
    __tablename__ = 'deals'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    amount: orm.Mapped[float] = orm.mapped_column(sa.Float, nullable=True)
    expected_close_date: orm.Mapped[sa.Date] = orm.mapped_column(sa.Date, nullable=True)
    stage: orm.Mapped[DealStage] = orm.mapped_column(
        postgresql.ENUM(DealStage, name="deal_stage", create_type=False),
        default=DealStage.QUALIFICATION,
        nullable=False
    )
    probability: orm.Mapped[float] = orm.mapped_column(sa.Float, default=0.0)
    lead_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("leads.id"), nullable=True)
    lead: orm.Mapped["Lead"] = orm.relationship("Lead", backref="deals")
    created_at: orm.Mapped[sa.DateTime] = orm.mapped_column(sa.DateTime, default=sa.func.now())
    updated_at: orm.Mapped[sa.DateTime] = orm.mapped_column(sa.DateTime, default=sa.func.now(), onupdate=sa.func.now())
    description: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    lost_reason: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)