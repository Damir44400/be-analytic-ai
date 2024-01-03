import os.path
from typing import List, Any
from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class CorsConfig(BaseSettings):
    CORS_ORIGINS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]
    CORS_METHODS: List[str] = ["*"]


class FormatConfig(BaseSettings):
    IMAGE_FORMATS: List[str] = ["png", 'jpg', "webp"]
    VIDEO_FORMATS: List[str] = ["mp4", "avi", "mkv", "mov", "mpeg"]


class DataConfig(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file="../.env")


class JWTConfig(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str

    model_config = SettingsConfigDict(env_file="../.env")


class PathConfig(BaseSettings):
    IMAGE_PATH: Any = os.path.join("media", 'images')
    VIDEO_PATH: Any = os.path.join("media", "videos")


class Config(FormatConfig, CorsConfig, JWTConfig, DataConfig, PathConfig):
    """Application configuration settings."""


env = Config()


class RootUserEmail(BaseSettings):
    ROOT_EMAIL: EmailStr
    ROOT_PASSWORD: str
    model_config = SettingsConfigDict(env_file="../.env")


fastapi_config: dict[str, Any] = {
    "title": "API",
}
