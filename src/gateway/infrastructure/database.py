from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.gateway.config import Config


def create_db_engine(config: Config) -> AsyncEngine:
    return create_async_engine(
        url=config.get_async_db_url
    )


def create_db_session(engine: AsyncEngine) -> async_sessionmaker:
    session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, autocommit=False)
    return session

@asynccontextmanager
async def get_db_session(session: async_sessionmaker) -> AsyncSession:
    async with session() as session:
        yield session


class Base(DeclarativeBase):
    pass
