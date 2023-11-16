from typing import Optional
from pydantic import BaseModel


class ProducerBase(BaseModel):
    name: str


class ProducerCreate(ProducerBase):
    pass


class ProducerUpdate(ProducerBase):
    pass
