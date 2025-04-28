import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.gateway.infrastructure.database import Base


class User(Base):
    __tablename__ = 'users'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    last_name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False, unique=True)
    password: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    is_staff: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, nullable=False, default=False)
