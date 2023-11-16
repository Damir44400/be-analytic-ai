from pydantic import BaseModel


class StudioBase(BaseModel):
    name: str


class StudioCreate(StudioBase):
    pass


class StudioUpdate(StudioBase):
    pass
