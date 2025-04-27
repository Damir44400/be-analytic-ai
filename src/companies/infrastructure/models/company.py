import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.gateway.infrastructure.database import Base

company_branches = sa.Table(
    'departments',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('generaal_company_id', sa.ForeignKey('companies.id')),
    sa.Column('branch_company_id', sa.ForeignKey('companies.id')),
)


class Company(Base):
    __tablename__ = 'companies'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    industry: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    sector: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    is_general: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, default=False)
    founded: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
