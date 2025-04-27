import pgvector as pgv
import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.gateway.infrastructure.database import Base


class CompanyData(Base):
    __tablename__ = 'companies_data'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    data: orm.Mapped[str] = orm.mapped_column(sa.String)
    file: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    vector_data: orm.Mapped[pgv.Vector] = orm.mapped_column(pgv.Vector())