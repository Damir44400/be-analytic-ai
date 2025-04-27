from dataclasses import dataclass


@dataclass
class RegisterRequest:
    email: str
    password: str


@dataclass
class RegisterResponse:
    user_id: int
    detail: str
