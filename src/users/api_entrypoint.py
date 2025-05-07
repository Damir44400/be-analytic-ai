from fastapi import APIRouter

from .presentation.api.auth import router as auth_router
from .presentation.api.user import router as user_router

router = APIRouter(prefix="/users")

router.include_router(auth_router, tags=["Auth"])
router.include_router(user_router, tags=["Profile"])
