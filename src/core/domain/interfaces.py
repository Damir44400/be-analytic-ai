from typing import Protocol


class IUoW(Protocol):
    async def _commit(self):
        pass

    async def _rollback(self):
        pass

    async def _close(self):
        pass
