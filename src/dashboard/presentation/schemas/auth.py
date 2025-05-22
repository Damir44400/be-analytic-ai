from pydantic import BaseModel, EmailStr


class UserBody(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class RegisterResponse(BaseModel):
    user_id: int
    detail: str


class UnauthorizedSchema(BaseModel):
    error: str = "User with this email not found"


class UserDataConflictSchema(BaseModel):
    error: str = "User with this email already exists"
