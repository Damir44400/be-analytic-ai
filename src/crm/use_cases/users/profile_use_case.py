from src.core.exceptions import UnauthorizedException
from src.crm.domain.entities.users import UserEntity
from src.crm.domain.interfaces.daos.users import IUserGetByIdDAO


class ProfileUseCase:
    def __init__(
            self,
            user_dao: IUserGetByIdDAO,
    ):
        self._user_dao = user_dao

    async def execute(self, user_id: int) -> UserEntity:
        db_user = await self._user_dao.get_user_by_id(user_id)
        if not db_user:
            raise UnauthorizedException("User with id {} not found".format(user_id))
        print(db_user)
        return db_user
