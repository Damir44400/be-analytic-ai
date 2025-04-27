from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class _LocalBaseSetting(BaseSettings):
    class Config:
        env_file = BASE_DIR / ".env"


class DataBaseConfig(_LocalBaseSetting):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def get_async_db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def get_db_url(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

class CorsConfig(_LocalBaseSetting):
    CORS_ORIGINS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    CORS_METHODS: List[str] = ["*"]


class JWTConfig(_LocalBaseSetting):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"
    JWT_ACCESS_SECRET_KEY: str = "MY SUPER"
    JWT_REFRESH_SECRET_KEY: str = "MY SUPER"


class Config(CorsConfig, JWTConfig, DataBaseConfig):
    """Application configuration settings."""
