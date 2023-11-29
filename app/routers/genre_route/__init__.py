from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.genre_repository import GenreRepository
from app.repositories.genre_anime_repository import GenreAnimeRepository

genre_anime_repo = GenreAnimeRepository()

genre_repo = GenreRepository()
router = APIRouter()

import_routers(__name__)
