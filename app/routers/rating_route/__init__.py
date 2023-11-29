from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.rating_repository import RatingRepository
from app.repositories.anime_repository import AnimeRepository

rating_repo = RatingRepository()
anime_repo = AnimeRepository()
router = APIRouter()

import_routers(__name__)
