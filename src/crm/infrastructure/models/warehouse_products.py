import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.crm.infrastructure.database.database import Base


class WarehouseProducts(Base):
    __tablename__ = "warehouse_products"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    product_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("products.id", ondelete="CASCADE")
    )
    warehouse_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "warehouses.id",
            ondelete="CASCADE"
        )
    )
