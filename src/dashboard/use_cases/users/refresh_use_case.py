import jwt

from src.core.exceptions import BadRequestException
from src.dashboard.domain.entities.jwt_payload import Payload
from src.dashboard.domain.interfaces.security.jwt_handler import IJwtService
from src.dashboard.presentation.schemas.auth import TokenResponse


class RefreshUseCase:
    def __init__(self, jwt_service: IJwtService):
        self._jwt_service = jwt_service

    async def execute(self, refresh_token: str) -> TokenResponse:
        try:
            payload: Payload = self._jwt_service.decode(refresh_token, _is_refresh=True)
        except jwt.ExpiredSignatureError:
            raise BadRequestException("Refresh expired")

        access_token = self._jwt_service.encode(payload)
        refresh_token = self._jwt_service.encode(payload, _is_refresh=True)
        return TokenResponse(access_token=access_token, refresh_token=refresh_token)
