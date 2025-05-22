from dataclasses import dataclass


@dataclass
class Token:
    token: str


@dataclass
class TokenResponse:
    access_token: Token
    refresh_token: Token
