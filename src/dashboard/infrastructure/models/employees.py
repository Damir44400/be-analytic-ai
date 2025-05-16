import enum

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class EmployeeStatusEnum(enum.Enum):
    ON_VACATION = "ON_VACATION"  # В отпуске
    ACTIVE = "ACTIVE"  # На работе
    ON_SICK_LEAVE = "ON_SICK_LEAVE"  # Больничный
    DISMISSED = "DISMISSED"  # Уволен
    ON_PROBATION = "ON_PROBATION"  # Испытательный срок
    TRAINING = "TRAINING"  # На обучении


class EmployeeRoleStatusEnum(enum.Enum):
    OWNER = "OWNER"
    EMPLOYEE = "EMPLOYEE"


class Employee(Base):
    __tablename__ = "employees"

    id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer, primary_key=True
    )
    user_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "users.id", ondelete="CASCADE"
        )
    )
    company_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "companies.id",
            ondelete="CASCADE"
        )
    )

    salary: orm.Mapped[float] = orm.mapped_column(
        sa.Float,
        default=0.0,
    )

    status: orm.Mapped[str] = orm.mapped_column(
        sa.Enum(
            EmployeeStatusEnum,
            name="employee_status"
        ),
        nullable=False,
        default=EmployeeStatusEnum.ACTIVE
    )

    role: orm.Mapped[str] = orm.mapped_column(
        sa.Enum(
            EmployeeRoleStatusEnum,
            name="employee_role"
        ),
        nullable=False,
        default=EmployeeRoleStatusEnum.EMPLOYEE
    )

    __table_args__ = (
        sa.UniqueConstraint(
            "user_id",
            "role"
        )
    )
