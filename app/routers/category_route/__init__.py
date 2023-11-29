from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.category_repository import CategoryRepository

category_repo = CategoryRepository()

router = APIRouter()

import_routers(__name__)
