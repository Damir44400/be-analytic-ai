from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.params import Depends

from src.crm.presentation.api.depends.authentication import get_current_user
from src.crm.domain.entities.users import UserEntity
from src.crm.domain.use_cases.users import IProfileUseCase, IProfileUpdateUseCase
from src.crm.presentation.schemas.user import UserProfile, UserProfileUpdate

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
