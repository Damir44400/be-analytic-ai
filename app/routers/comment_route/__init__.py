from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.anime_repository import AnimeRepository
from app.repositories.comment_repository import CommentRepository

anime_repo = AnimeRepository()
comment_repo = CommentRepository()

router = APIRouter()

import_routers(__name__)
