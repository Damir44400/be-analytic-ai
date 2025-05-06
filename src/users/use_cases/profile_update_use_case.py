from src.core.domain.interfaces import IUoW
from src.users.domain.entities import UserEntity
from src.users.domain.exeptions import UnauthorizedException
from src.users.domain.use_cases.profile.entities import Profile
from src.users.domain.use_cases.profile.interfaces import IProfileUpdateUseCase, UserGetUpdateGateway


class ProfileUpdateUseCase(IProfileUpdateUseCase):
    def __init__(
            self,
            uow: IUoW,
            user_dao: UserGetUpdateGateway,
    ):
        self._uow = uow
        self._user_dao = user_dao

    async def execute(self, user_id: int, profile: Profile) -> UserEntity:
        db_user = await self._user_dao.get_user_by_id(user_id)
        if not db_user:
            raise UnauthorizedException("User with id {} not found".format(user_id))
        async with self._uow:
            updated_user = await self._user_dao.update_user(user_id, UserEntity(
                first_name=profile.first_name,
                last_name=profile.last_name,
            ))
        return updated_user
