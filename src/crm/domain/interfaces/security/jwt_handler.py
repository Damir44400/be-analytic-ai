from typing import Protocol

from src.crm.domain.entities.jwt_payload import Payload
from src.crm.domain.entities.tokens import Token


class IJwtService(Protocol):
    def encode(self, payload: Payload, _is_refresh: bool = False) -> Token:
        pass

    def decode(self, token: str, _is_refresh: bool = False) -> Payload:
        pass
