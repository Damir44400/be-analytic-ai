from typing import List

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.params import Depends

from src.core.authentication import get_current_user
from src.dashboard.domain.use_cases.companies import (
    IRegisterCompanyUseCase,
    CompanyRegisterForm,
    IUpdateCompanyUseCase,
    IDeleteCompanyUseCase,
    IGetCompanyDetailUseCase,
    CompanyUpdateForm
)
from src.users.domain.entities import UserEntity
from ..schemas.companies import (
    CompanyCreate,
    UserCompaniesRead,
    CompanyRead,
    CompanyUpdate,
    CompanyReadBranch
)
from ...domain.use_cases.companies import IGetUserCompaniesUseCase

router = APIRouter()


@router.post("/", responses={
    200: {
        "content": {
            "application/json": {
                "example": {
                    "detail": "Successfully registered company"
                }
            }
        }
    }
})
@inject
async def create_company(
        form: CompanyCreate,
        use_case: FromDishka[IRegisterCompanyUseCase],
        auth_user: UserEntity = Depends(get_current_user)):
    return await use_case.execute(
        CompanyRegisterForm(**form.dict()),
        auth_user.id
    )


@router.get("/", response_model=List[UserCompaniesRead])
@inject
async def get_user_companies(
        use_case: FromDishka[IGetUserCompaniesUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(auth_user.id)


@router.get("/{company_id}", response_model=CompanyReadBranch)
@inject
async def get_company_detail(
        company_id: int,
        use_case: FromDishka[IGetCompanyDetailUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(user_id=auth_user.id, company_id=company_id)


@router.patch("/{company_id}", response_model=CompanyRead)
@inject
async def update_company(
        company_id: int,
        form: CompanyUpdate,
        use_case: FromDishka[IUpdateCompanyUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(company_id, CompanyUpdateForm(**form.dict()), auth_user.id)


@router.delete("/{company_id}", status_code=200)
@inject
async def delete_company(
        company_id: int,
        use_case: FromDishka[IDeleteCompanyUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(company_id, auth_user.id)
