from typing import Any

from pydantic import BaseModel


class TokenPayload(BaseModel):
    sub: Any = None
    exp: Any = None


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class AccessSchema(BaseModel):
    access_token: str


class RefreshSchema(BaseModel):
    refresh_token: str
