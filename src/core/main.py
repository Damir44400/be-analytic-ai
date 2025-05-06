from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.core.di.app_provider import create_container
from src.users.domain.exeptions import UserBaseException
from src.users.api_entrypoint import register_user_base_exception_handler, router as user_router

app = FastAPI()
container = create_container()

setup_dishka(app=app, container=container)

app.include_router(user_router, prefix="/api/v1")

app.add_exception_handler(UserBaseException, register_user_base_exception_handler)
