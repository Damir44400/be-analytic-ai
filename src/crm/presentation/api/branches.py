from typing import List

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.params import Depends

from src.crm.presentation.api.depends.authentication import get_current_user
from src.crm.domain.use_cases.branches import (
    IRegisterCompanyBranchUseCase,
    CompanyBranchRegisterForm,
    IUpdateCompanyBranchUseCase,
    IDeleteCompanyBranchUseCase,
    CompanyBranchUpdateForm
)
from ..schemas.branches import (
    CompanyBranchCreate,
    CompanyBranchRead,
    CompanyBranchUpdate
)
from ...domain.entities.users import UserEntity
from ...domain.use_cases.branches import IGetCompanyBranchesUseCase

router = APIRouter()


@router.post("/", responses={
    200: {
        "content": {
            "application/json": {
                "example": {
                    "detail": "Successfully registered company branch"
                }
            }
        }
    }
})
@inject
async def create_company_branch(
        form: CompanyBranchCreate,
        use_case: FromDishka[IRegisterCompanyBranchUseCase],
        auth_user: UserEntity = Depends(get_current_user)):
    return await use_case.execute(
        CompanyBranchRegisterForm(**form.dict()),
        auth_user.id
    )


@router.get("/", response_model=List[CompanyBranchRead])
@inject
async def get_company_branches(
        use_case: FromDishka[IGetCompanyBranchesUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(auth_user.id)


@router.patch("/{branch_id}", response_model=CompanyBranchRead)
@inject
async def update_company_branch(
        branch_id: int,
        form: CompanyBranchUpdate,
        use_case: FromDishka[IUpdateCompanyBranchUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(branch_id, CompanyBranchUpdateForm(**form.dict()), auth_user.id)


@router.delete("/{branch_id}", status_code=200)
@inject
async def delete_company_branch(
        branch_id: int,
        use_case: FromDishka[IDeleteCompanyBranchUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(branch_id, auth_user.id)
