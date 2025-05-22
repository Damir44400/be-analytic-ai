from src.core.exceptions import UnauthorizedException, BadRequestException
from src.dashboard.domain.entities.jwt_payload import Payload
from src.dashboard.domain.entities.tokens import Token, TokenResponse
from src.dashboard.domain.entities.users import UserEntity
from src.dashboard.domain.interfaces.daos.users import IUserGetByEmailDAO
from src.dashboard.domain.interfaces.security.jwt_handler import IJwtService
from src.dashboard.domain.interfaces.security.password_handler import IPasswordBcrypt


class LoginUseCase:
    def __init__(
            self,
            user_dao: IUserGetByEmailDAO,
            password_bcrypt: IPasswordBcrypt,
            jwt_service: IJwtService
    ):
        self._user_dao = user_dao
        self._password_bcrypt = password_bcrypt
        self._jwt_service = jwt_service

    async def execute(self, user: UserEntity) -> TokenResponse:
        db_user = await self._user_dao.get_user_by_email(user.email)
        if not db_user:
            raise UnauthorizedException("User with this email not found")
        try:
            check_pw = (
                self
                ._password_bcrypt
                .verify_password(
                    user.password.encode("utf-8"),
                    db_user.password.encode("utf-8")
                )
            )
        except Exception as e:
            raise BadRequestException(str(e))
        if not check_pw:
            raise UnauthorizedException("Password does not match")

        access_token: Token = self._jwt_service.encode(Payload(user_id=db_user.id))
        refresh_token: Token = (
            self
            ._jwt_service
            .encode(
                Payload(
                    user_id=db_user.id
                ),
                _is_refresh=True
            )
        )

        return TokenResponse(access_token, refresh_token)
