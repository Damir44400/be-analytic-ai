import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class User(Base):
    __tablename__ = 'users'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    last_name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False, unique=True)
    password: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
