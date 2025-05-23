from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.interfaces.uow import IUoW


class UoW(IUoW):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def _commit(self):
        await self._session.commit()

    async def _rollback(self):
        await self._session.rollback()

    async def _close(self):
        await self._session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self._rollback()
        else:
            await self._commit()
        await self._session.close()
