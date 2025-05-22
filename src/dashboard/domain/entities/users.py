from dataclasses import dataclass
from typing import Optional

from src.core.domain.entity import EntityMeta


@dataclass
class UserEntity(EntityMeta):
    id: Optional[int] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    is_staff: Optional[bool] = None
    is_employee: Optional[bool] = None

    class Meta:
        exclude_none = True
