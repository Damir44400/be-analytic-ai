from typing import List, Optional
from pydantic import BaseModel, DateTime


class AnimeBase(BaseModel):
    title: str
    date_announce: Optional[DateTime]
    country: Optional[str]
    description: str


class AnimeCreate(AnimeBase):
    studio_id: int
    producer_id: int


class AnimeUpdate(AnimeBase):
    pass


class AnimeChapterCreate(BaseModel):
    anime_video: str
    anime_id: int
