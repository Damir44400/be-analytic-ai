from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from pydantic.types import SecretStr
from fastapi import UploadFile


class UserBase(BaseModel):
    username: Optional[str]


class UserRegistration(UserBase):
    email: Optional[EmailStr]
    password: Optional[SecretStr]


class UserProfile(UserBase):
    id: int
    profile_photo: Optional[str]
    registered_at: Optional[datetime]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        datetime_format = "%Y-%m-%dT%H:%M:%S"


class UserUpdate(UserBase):
    profile_photo: Optional[Annotated[str, UploadFile]]
    email: Optional[EmailStr]
    password: Optional[SecretStr]