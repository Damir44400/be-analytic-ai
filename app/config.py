from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
import importlib
import pkgutil

from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    CORS_ORIGINS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    CORS_METHODS: List[str] = ["*"]

    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file="../.env")


env = Config()


def import_routers(package_name):
    """import routes"""
    package = importlib.import_module(package_name)
    prefix = package.__name__ + "."

    for _, module_name, _ in pkgutil.iter_modules(package.__path__, prefix):
        if not module_name.startswith(prefix + "router_"):
            continue

        try:
            importlib.import_module(module_name)
        except Exception as e:
            print(f"Failed to import {module_name}, error: {e}")
