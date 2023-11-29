from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.date_created_repository import AnimeDateCreatedRepository

announce_repo = AnimeDateCreatedRepository()

router = APIRouter()

import_routers(__name__)
