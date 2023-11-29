from typing import Optional
from pydantic import BaseModel


class ProducerBase(BaseModel):
    name: str


class ProducerCreate(ProducerBase):
    pass


class ProducerUpdate(ProducerBase):
    pass


class Producer(ProducerBase):
    id: int

    class Config:
        from_attributes = True
