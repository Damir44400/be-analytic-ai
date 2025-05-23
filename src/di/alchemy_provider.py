from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession

from src.config import Config
from src.crm.domain.interfaces.uow import IUoW
from src.crm.infrastructure.database.database import create_db_engine, create_db_session
from src.crm.infrastructure.database.uow import UoW


class AlchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def get_async_engine(self, config: Config) -> AsyncEngine:
        return create_db_engine(config)

    @provide(scope=Scope.REQUEST)
    def get_async_session(self, engine: AsyncEngine) -> async_sessionmaker:
        return create_db_session(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_factory: async_sessionmaker) -> AsyncIterable[AsyncSession]:
        async with session_factory() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_uow(self, session: AsyncSession) -> IUoW:
        return UoW(session)
