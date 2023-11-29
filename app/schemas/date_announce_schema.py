from pydantic import BaseModel


class AnnounceSchemaBase(BaseModel):
    year: int


class AnnounceSchema(AnnounceSchemaBase):
    id: int
