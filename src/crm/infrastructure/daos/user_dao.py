from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.crm.domain.entities.users import UserEntity
from src.crm.infrastructure.models.users import User


class UserDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_by_id(self, id: int) -> UserEntity:
        stmt = select(User).where(User.id == id)
        user = await self._session.execute(stmt)
        user = user.scalars().first()
        return UserEntity.to_domain(user)

    async def get_user_by_email(self, email: str) -> UserEntity:
        stmt = select(User).where(User.email == email)
        user = await self._session.execute(stmt)
        user = user.scalars().first()
        return UserEntity.to_domain(user)

    async def create_user(self, user: UserEntity) -> UserEntity:
        stmt = insert(User).values(**user.to_dict()).returning(User)
        user = await self._session.execute(stmt)
        user = user.scalars().first()
        return UserEntity.to_domain(user)

    async def update_user(self, user_id: int, user: UserEntity) -> UserEntity:
        stmt = update(User).values(**user.to_dict()).where(User.id == user_id).returning(User)
        user = await self._session.execute(stmt)
        user = user.scalars().first()
        return UserEntity.to_domain(user)
