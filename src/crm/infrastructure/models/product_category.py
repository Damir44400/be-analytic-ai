import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class ProductsCategory(Base):
    __tablename__ = "product_categories"
    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    category_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "categories.id",
            ondelete="CASCADE"
        )
    )
    product_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "products.id",
            ondelete="CASCADE"
        )
    )

    __table_args__ = tuple(
        sa.UniqueConstraint(
            "category_id",
            "product_id",
        )
    )
