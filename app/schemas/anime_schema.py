from typing import Optional, List
from pydantic import BaseModel


class AnimeBase(BaseModel):
    title: str
    cover: str
    date_announced: Optional[int]
    country: Optional[str] = "Japan"
    description: str


class AnimeCreate(AnimeBase):
    category_id: Optional[int]
    studio_id: Optional[int] = None


class AnimeUpdate(AnimeBase):
    category_id: Optional[int]
    studio_id: Optional[int] = None


class Anime(BaseModel):
    id: Optional[int]
    cover: str
    title: str
    description: str
    category: Optional[dict]
    date_announced: Optional[int]
    genres: List[dict]
    country: Optional[str] = "Japan"
    studio: Optional[dict] = None

    class Config:
        from_attributes = True


class AnimeChapterBase(BaseModel):
    anime_video_url: str


class AnimeChapterCreate(AnimeChapterBase):
    pass


class GetAnimeChapter(AnimeChapterBase):
    id: int

    class Config:
        from_attributes = True
