from dataclasses import Field
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from app.models.models import Anime


class AnimeFilter(Filter):
    name__in: Optional[list[str]] = Field(alias="names")
    quantity__lte: Optional[int] = Field(alias="quantityTo")

    class Constants(Filter.Constants):
        model = Anime

    class Config:
        allow_population_by_field_name = True
