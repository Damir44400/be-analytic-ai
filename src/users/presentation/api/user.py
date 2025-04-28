from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.params import Depends

from src.gateway.authentication import get_current_user
from src.users.domain.entities import UserEntity
from src.users.domain.use_cases.profile.interfaces import IProfileUseCase, IProfileUpdateUseCase
from src.users.presentation.schemas.user import UserProfile, UserProfileUpdate

router = APIRouter()


@router.get("/me", response_model=UserProfile)
@inject
async def get_profile(
        use_case: FromDishka[IProfileUseCase],
        current_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(current_user.id)


@router.patch("/me", response_model=UserProfile)
@inject
async def update_profile(
        form: UserProfileUpdate,
        use_case: FromDishka[IProfileUpdateUseCase],
        current_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(current_user.id, UserEntity(**form.dict()))
