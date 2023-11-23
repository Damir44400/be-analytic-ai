from fastapi import APIRouter
from app.utils.utils import import_routers
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.database import engine

user_repo = UserRepository()

router = APIRouter()
role_repo = RoleRepository(engine)
import_routers(__name__)

