from fastapi import UploadFile
from typing import Optional, List, Dict
from pydantic import BaseModel
from datetime import datetime


class AnimeBase(BaseModel):
    title: str
    cover: str
    date_announce: Optional[int]
    country: Optional[str] = "Japan"
    description: str


class AnimeCreate(AnimeBase):
    category_id: Optional[int]
    studio_id: Optional[int] = None
    producer_id: Optional[int] = None


class AnimeUpdate(AnimeBase):
    category_id: Optional[int]
    studio_id: Optional[int] = None
    producer_id: Optional[int] = None


class Anime(BaseModel):
    id: Optional[int]
    cover: str
    title: str
    description: str
    category: Optional[str]
    date_announce: Optional[int]
    genres: list
    country: Optional[str] = "Japan"
    studio: Optional[str] | None
    producer: Optional[str] | None
    date_uploaded: Optional[datetime]
    date_updated: Optional[datetime]

    class Config:
        from_attributes = True


class AnimeChapterCreate(BaseModel):
    anime_videos: str
    anime_title: str
    chapter: int


class GetAnimeChapter(BaseModel):
    id: int

    class Config:
        from_attributes = True
