from src.core.domain.interfaces import IUoW
from src.dashboard.domain.entities.users import UserEntity
from src.dashboard.domain.interfaces.daos.users import IUserUpdateUserDAO


class ProfileUpdateUseCase:
    def __init__(
            self,
            uow: IUoW,
            user_dao: IUserUpdateUserDAO,
    ):
        self._uow = uow
        self._user_dao = user_dao

    async def execute(self, user_id: int, profile: UserEntity) -> UserEntity:
        async with self._uow:
            updated_user = await self._user_dao.update_user(user_id, UserEntity(
                first_name=profile.first_name,
                last_name=profile.last_name,
            ))
        return updated_user
