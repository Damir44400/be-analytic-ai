from dataclasses import dataclass

from src.users.domain.entities import Token


@dataclass
class TokenResponse:
    access_token: Token
    refresh_token: Token


@dataclass
class LoginRequest:
    email: str
    password: str
