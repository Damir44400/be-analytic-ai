from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from .domain.exeptions import UserBaseException
from .presentation.api.auth import router as auth_router

router = APIRouter(prefix="/users")

router.include_router(auth_router, tags=["Auth"])


def register_user_base_exception_handler(request: Request, exc: UserBaseException):
    return JSONResponse({"error": str(exc)}, status_code=exc.status_code)