from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_superuser: bool = False
    is_representative: bool = False

    class Config:
        orm_mode = True
