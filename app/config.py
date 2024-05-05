from typing import List, Any
from pydantic_settings import BaseSettings, SettingsConfigDict


class CorsConfig(BaseSettings):
    CORS_ORIGINS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    CORS_METHODS: List[str] = ["*"]


class JWTConfig(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str = "MY SUPER"
    JWT_REFRESH_SECRET_KEY: str = "MY SUPER"


class Config(CorsConfig, JWTConfig):
    """Application configuration settings."""


env = Config()

fastapi_config: dict[str, Any] = {
    "title": "API",
}
