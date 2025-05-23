from typing import List

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.params import Depends

from src.crm.domain.use_cases.categories import (
    ICategoryCreateUseCase,
    ICategoryUpdateUseCase,
    ICategoryDeleteUseCase, ICompanyCategoryListUseCase,
)
from src.crm.presentation.api.depends.authentication import get_current_user
from ..schemas.categories import (
    CompanyCategoryCreate,
    CompanyCategoryRead,
    CompanyCategoryUpdate
)
from ...domain.entities.categories import CategoryEntity
from ...domain.entities.users import UserEntity

router = APIRouter()


@router.post("/", responses={
    200: {
        "content": {
            "application/json": {
                "example": {
                    "detail": "Successfully registered company category"
                }
            }
        }
    }
})
@inject
async def create_company_category(
        form: CompanyCategoryCreate,
        use_case: FromDishka[ICategoryCreateUseCase],
        auth_user: UserEntity = Depends(get_current_user)):
    return await use_case.execute(
        CategoryEntity(**form.dict()),
        auth_user.id
    )


@router.get("/", response_model=List[CompanyCategoryRead])
@inject
async def get_company_categories(
        use_case: FromDishka[ICompanyCategoryListUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(auth_user.id)


@router.patch("/{category_id}", response_model=CompanyCategoryRead)
@inject
async def update_company_category(
        category_id: int,
        form: CompanyCategoryUpdate,
        use_case: FromDishka[ICategoryUpdateUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(category_id, CategoryEntity(**form.dict()), auth_user.id)


@router.delete("/{category_id}", status_code=200)
@inject
async def delete_company_category(
        category_id: int,
        use_case: FromDishka[ICategoryDeleteUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(category_id, auth_user.id)
