from fastapi import APIRouter
from app.utils.utils import import_routers
from app.repositories.user_repository import UserRepository

router = APIRouter()
user_repo = UserRepository()
import_routers(__name__)
