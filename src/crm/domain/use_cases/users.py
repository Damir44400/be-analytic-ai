from typing import Protocol, Dict

from src.crm.domain.entities.tokens import TokenResponse
from src.crm.domain.entities.users import UserEntity


class ILoginUseCase(Protocol):
    async def execute(self, user: UserEntity) -> TokenResponse:
        pass


class IProfileUseCase(Protocol):
    async def execute(self, user_id: int) -> UserEntity:
        pass


class IProfileUpdateUseCase(Protocol):
    async def execute(self, user_id: int, form: UserEntity) -> UserEntity:
        pass


class IRefreshUseCase(Protocol):
    async def execute(self, refresh_token: str) -> TokenResponse:
        pass


class IRegisterUseCase(Protocol):
    async def execute(self, user: UserEntity) -> Dict[str, str]:
        pass
