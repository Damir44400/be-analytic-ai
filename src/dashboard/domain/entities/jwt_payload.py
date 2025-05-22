from dataclasses import dataclass
from typing import Optional


@dataclass
class Payload:
    user_id: int
    exp: Optional[int] = None