from fastapi import APIRouter
from app.utils.utils import import_routers
from app.repositories.user_repository import UserRepository
from app.repositories.comment_repository import CommentRepository
from app.repositories.anime_repository import AnimeRepository

router = APIRouter()
user_repo = UserRepository()
comment_repo = CommentRepository()
anime_repo = AnimeRepository()
import_routers(__name__)
