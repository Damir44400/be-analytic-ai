from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, EmailStr
from fastapi import UploadFile


class UserBase(BaseModel):
    username: str


class UserRegistration(UserBase):
    email: Optional[EmailStr]
    password: Optional[str]


class UserProfile(UserBase):
    id: int
    profile_photo: str
    registered_at: datetime
    is_active: bool

    class Config:
        datetime_format = "%Y-%m-%d"


class UserUpdate(UserBase):
    email: EmailStr | None
    password: str | None


class UserOut(UserBase):
    id: int
    is_active: bool
