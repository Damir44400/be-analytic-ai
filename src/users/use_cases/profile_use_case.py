from src.users.domain.entities import UserEntity
from src.core.exeptions import UnauthorizedException
from src.users.domain.use_cases.profile.interfaces import IProfileUseCase, UserGetGateway


class ProfileUseCase(IProfileUseCase):
    def __init__(
            self,
            user_dao: UserGetGateway,
    ):
        self._user_dao = user_dao

    async def execute(self, user_id: int) -> UserEntity:
        db_user = await self._user_dao.get_user_by_id(user_id)
        if not db_user:
            raise UnauthorizedException("User with id {} not found".format(user_id))
        print(db_user)
        return db_user
