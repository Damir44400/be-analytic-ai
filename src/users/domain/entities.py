from dataclasses import dataclass
from typing import Optional

from src.gateway.domain.entity import EntityMeta


@dataclass
class UserEntity(EntityMeta):
    id: Optional[int] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[bytes] = None
    is_staff: Optional[bool] = None

    class Meta:
        exclude_none = True


@dataclass
class Token:
    token: str


@dataclass
class Payload:
    user_id: int
    exp: Optional[int] = None
