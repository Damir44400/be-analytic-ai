import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class Category(Base):
    __tablename__ = "categories"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String, index=True)
    company_id: orm.Mapped[int] = orm.mapped_column(sa.Integer)

    __table_args__ = tuple(
        sa.UniqueConstraint("company_id", "name")
    )
