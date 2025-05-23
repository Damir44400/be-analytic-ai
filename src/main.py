from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from src.di.app_provider import create_container
from src.crm.domain.exceptions import AppBaseException
from src.crm.presentation.api import router as dashboard_router

app = FastAPI()
container = create_container()

setup_dishka(app=app, container=container)

app.include_router(dashboard_router, prefix="/api/v1")


@app.exception_handler(AppBaseException)
async def app_exception_handler(request: Request, exc: AppBaseException):
    return JSONResponse({"detail": str(exc)}, status_code=exc.status_code)
