from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.genre_repository import GenreRepository
from app.repositories.anime_repository import AnimeRepository

anime_repo = AnimeRepository()

genre_repo = GenreRepository()
router = APIRouter()

import_routers(__name__)
