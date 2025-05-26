import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.crm.infrastructure.database.database import Base


class CompanyBranch(Base):
    __tablename__ = "company_branches"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String, unique=True)
    city: orm.Mapped[str] = orm.mapped_column(sa.String)
    country: orm.Mapped[str] = orm.mapped_column(sa.String)
    address: orm.Mapped[str] = orm.mapped_column(sa.String)
    company_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "companies.id",
            ondelete="CASCADE"
        )
    )
    company = orm.relationship("Company", backref="branches")
