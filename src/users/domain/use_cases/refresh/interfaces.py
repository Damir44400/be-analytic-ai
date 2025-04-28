from typing import Protocol

from src.users.presentation.schemas.auth import TokenResponse


class IRefreshUseCase(Protocol):
    async def execute(self, refresh_token: str) -> TokenResponse:
        pass
