import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.dialects import postgresql
from src.crm.infrastructure.database.database import Base


class EmployeeRole(Base):
    __tablename__ = 'employee_role'

    id: orm.Mapped[int] = sa.