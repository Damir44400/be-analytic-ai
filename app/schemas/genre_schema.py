from pydantic import BaseModel


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        from_attributes = True


class GenreAnimeBase(BaseModel):
    pass


class GenreAnimeCreate(GenreAnimeBase):
    genre_id: int
    anime_id: int


class GenreAnime(GenreAnimeBase):
    id: int
    genre_id: int
    anime_id: int

    class Config:
        from_attributes = True
