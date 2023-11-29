from pydantic import BaseModel
from enum import Enum


class StudioBase(BaseModel):
    name: str


class StudioCreate(StudioBase):
    pass


class StudioUpdate(StudioBase):
    pass


class Studio(StudioBase):
    id: int

    class Config:
        from_attributes = True
