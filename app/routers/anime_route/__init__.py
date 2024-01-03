from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.anime_repository import AnimeRepository
from app.repositories.studio_repository import StudioRepository
from app.repositories.anime_chapter_repository import AnimeChapterRepository
from app.repositories.genre_repository import GenreRepository
from app.repositories.genre_of_anime_repository import GenreAnimeRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.rating_repository import RatingRepository
from app.repositories.comment_repository import CommentRepository
from app.repositories.user_repository import UserRepository

anime_repo = AnimeRepository()
studio_repo = StudioRepository()
chapter_repo = AnimeChapterRepository()
genre_repo = GenreRepository()
genre_anime_repo = GenreAnimeRepository()
category_repo = CategoryRepository()
rating_repo = RatingRepository()
comment_repo = CommentRepository()
user_repo = UserRepository()

router = APIRouter()

import_routers(__name__)
