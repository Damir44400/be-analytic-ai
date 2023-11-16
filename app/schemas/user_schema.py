from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: Optional[str]


class UserRegistration(UserBase):
    email: Optional[EmailStr]
    password: Optional[str]


class UserProfile(UserBase):
    id: int
    profile_photo: Optional[str] = None
    registered_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool]
    is_moderator: Optional[bool]

    class Config:
        datetime_format = "%Y-%m-%d"


class UserUpdate(BaseModel):
    username: str | None
    email: EmailStr | None
    profile_photo: str | None
    password: str | None


class UserOut(UserBase):
    id: int
    is_active: Optional[bool] = False
    is_superuser: Optional[bool]
    is_moderator: Optional[bool]
