from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.anime_repository import AnimeRepository
from app.repositories.studio_repository import StudioRepository
from app.repositories.anime_chapter_repository import AnimeChapterRepository
from app.repositories.producer_repository import ProducerRepository
from app.repositories.genre_repository import GenreRepository
from app.repositories.genre_anime_repository import GenreAnimeRepository

anime_repo = AnimeRepository()
studio_repo = StudioRepository()
chapter_repo = AnimeChapterRepository()
producer_repo = ProducerRepository()
genre_repo = GenreRepository()
genre_anime_repo = GenreAnimeRepository()
router = APIRouter()

import_routers(__name__)
