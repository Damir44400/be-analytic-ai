from fastapi import APIRouter
from app.utils.utils import import_routers

from app.repositories.producer_repository import ProducerRepository

producer_repo = ProducerRepository()
router = APIRouter()

import_routers(__name__)
