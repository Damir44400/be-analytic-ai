from pydantic import BaseModel


class UnauthorizedSchema(BaseModel):
    error: str = "User with this email not found"


class UserDataConflictSchema(BaseModel):
    error: str = "User with this email already exists"
