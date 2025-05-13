import enum

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class BusinessTypeEnum(enum.Enum):
    SOLE_PROPRIETORSHIP = "IP"
    JOIN_STOCK_COMPANY = "JSC"
    LIMITED_LIABILITY_COMPANY = "TOO"


class BusinessActivityEnum(enum.Enum):
    PHYSICAL_COMPANY = "PHYSICAL"
    DIGITAL_COMPANY = "DIGITAL"


class Company(Base):
    __tablename__ = "companies"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    company_logo: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    company_name: orm.Mapped[str] = orm.mapped_column(sa.String, index=True)
    business_type: orm.Mapped[BusinessTypeEnum] = orm.mapped_column(
        sa.Enum(BusinessTypeEnum),
        default=BusinessTypeEnum.SOLE_PROPRIETORSHIP
    )
    description: orm.Mapped[str] = orm.mapped_column(sa.String)
    company_website: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    company_phone_number: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    user_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("users.id"))

    user = orm.relationship("User", backref="companies")
