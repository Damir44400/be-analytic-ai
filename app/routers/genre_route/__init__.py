from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.genre_repository import GenreRepository
from app.repositories.genre_of_anime_repository import GenreAnimeRepository
from app.repositories.anime_repository import AnimeRepository
from app.repositories.category_repository import CategoryRepository

genre_anime_repo = GenreAnimeRepository()

genre_repo = GenreRepository()
router = APIRouter()
anime_repo = AnimeRepository()
category_repo = CategoryRepository()

import_routers(__name__)
