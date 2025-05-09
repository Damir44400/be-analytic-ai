import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class Product(Base):
    __tablename__ = "products"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)
    type: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    price: orm.Mapped[float] = orm.mapped_column(sa.Float, nullable=False)
    branch_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("company_branches.id"), nullable=False)

    branch = orm.relationship("CompanyBranch", back_populates="products")
