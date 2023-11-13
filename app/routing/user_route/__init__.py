from fastapi import APIRouter
from app.config import import_routers
from app.repositories.user_repository import UserRepository
from app.schemas import user_schema

router = APIRouter()
user_repo = UserRepository()
import_routers(__name__)
