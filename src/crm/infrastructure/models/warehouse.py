import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.crm.infrastructure.database.database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String)
    address: orm.Mapped[str] = orm.mapped_column(sa.String)
    branch_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("company_branches.id"))

    branch = orm.relationship("CompanyBranch", backref="warehouses")
