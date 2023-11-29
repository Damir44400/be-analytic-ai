from pydantic import BaseModel, validator


class RatingBase(BaseModel):
    stars: int
    anime_id: int


class RatingCreate(RatingBase):
    @validator('stars')
    def validate_stars(cls, star):
        if 1 <= star <= 5:
            return star
        raise ValueError('The rating range is 1 to 5')


class RatingUpdate(RatingCreate):
    pass


class Rating(RatingBase):
    id: int

    class Config:
        from_attributes = True
