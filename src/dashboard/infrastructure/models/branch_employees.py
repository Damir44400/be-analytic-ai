import enum

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class EmployeesEnum(enum.Enum):
    ON_VACATION = "ON_VACATION"  # В отпуске
    ACTIVE = "ACTIVE"  # На работе
    ON_SICK_LEAVE = "ON_SICK_LEAVE"  # Больничный
    DISMISSED = "DISMISSED"  # Уволен
    ON_PROBATION = "ON_PROBATION"  # Испытательный срок
    TRAINING = "TRAINING"  # На обучении


class BranchEmployees(Base):
    __tablename__ = "branch_employees"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    user_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("users.id", ondelete="CASCADE")
    )
    branch_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("company_branches.id", ondelete="CASCADE")
    )

    salary: orm.Mapped[float] = orm.mapped_column(
        sa.Float,
        default=0.0,
    )

    status: orm.Mapped[str] = orm.mapped_column(
        sa.Enum(
            EmployeesEnum,
            name="employee_status"
        ),
        nullable=False,
        default=EmployeesEnum.ACTIVE
    )

    branch = orm.relationship(
        "CompanyBranch",
        back_populates="employees",
    )
