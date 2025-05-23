from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.crm.infrastructure.database.database import Base


class WarehouseTransfer(Base):
    __tablename__ = "warehouse_transfers"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)

    product_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False
    )

    from_warehouse_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("warehouses.id", ondelete="CASCADE"),
        nullable=False
    )

    to_warehouse_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("warehouses.id", ondelete="CASCADE"),
        nullable=False
    )

    quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)

    transfer_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    comment: orm.Mapped[str] = orm.mapped_column(sa.Text, nullable=True)

    product = orm.relationship(
        "Product",
        backref="transfers"
    )
    from_warehouse = orm.relationship(
        "Warehouse",
        foreign_keys=[from_warehouse_id],
        backref="outgoing_transfers"
    )
    to_warehouse = orm.relationship(
        "Warehouse",
        foreign_keys=[to_warehouse_id],
        backref="incoming_transfers"
    )
