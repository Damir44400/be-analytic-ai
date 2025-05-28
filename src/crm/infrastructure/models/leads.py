import enum

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.dialects import postgresql

from src.crm.infrastructure.database.database import Base


class LeadStatus(enum.Enum):
    NEW = "New"
    ATTEMPTING_CONTACT = "Attempting Contact"
    CONTACTED = "Contacted"
    ENGAGED = "Engaged"
    QUALIFIED = "Qualified"
    NOT_INTERESTED = "Not Interested"
    UNQUALIFIED = "Unqualified"
    BAD_CONTACT_INFO = "Bad Contact Info"
    NO_RESPONSE = "No Response"
    CONVERTED = "Converted"


class Lead(Base):
    __tablename__ = 'leads'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    email: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    phone_number: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    source: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    status: orm.Mapped[LeadStatus] = orm.mapped_column(
        postgresql.ENUM(LeadStatus, name="lead_status", create_type=False),
        default=LeadStatus.NEW,
        nullable=False
    )
    created_at: orm.Mapped[sa.DateTime] = orm.mapped_column(sa.DateTime, default=sa.func.now())
    updated_at: orm.Mapped[sa.DateTime] = orm.mapped_column(sa.DateTime, default=sa.func.now(), onupdate=sa.func.now())

    product_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("products.id"))
    product: orm.Mapped["Product"] = orm.relationship("Product", backref="leads")

    comments: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
