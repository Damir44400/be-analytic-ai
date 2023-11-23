from fastapi import UploadFile
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class AnimeBase(BaseModel):
    title: str
    cover: str
    date_announce: Optional[datetime] | str = "Announced"
    country: Optional[str] = "Japan"
    description: str


class AnimeCreate(AnimeBase):
    studio_id: Optional[int] = None
    producer_id: Optional[int] = None


class AnimeUpdate(AnimeBase):
    pass


class AnimeChapterCreate(BaseModel):
    anime_videos: List[UploadFile]
    anime_id: int
