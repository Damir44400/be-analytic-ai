from typing import Optional

from pydantic import BaseModel


class BaseUserProfile(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str


class UserProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserProfile(BaseUserProfile):
    id: int

    class Meta:
        from_attributes = True
