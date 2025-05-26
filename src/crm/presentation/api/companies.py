from typing import List

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.params import Depends, Query

from src.crm.domain.use_cases.companies import (
    IRegisterCompanyUseCase,
    CompanyRegisterForm,
    IUpdateCompanyUseCase,
    IDeleteCompanyUseCase,
    IGetCompanyDetailUseCase,
    CompanyUpdateForm
)
from src.crm.presentation.api.depends.authentication import get_current_user
from ..schemas.branches import CompanyBranchRead
from ..schemas.companies import (
    CompanyCreate,
    UserCompaniesRead,
    CompanyRead,
    CompanyUpdate
)
from ..schemas.products import ProductRead
from ...domain.entities.users import UserEntity
from ...domain.use_cases.branches import IGetCompanyBranchesUseCase
from ...domain.use_cases.companies import IGetUserCompaniesUseCase
from ...domain.use_cases.products import IProductListByCompanyUseCase

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


@router.get("/{company_id}", response_model=CompanyRead)
@inject
async def get_company_detail(
        company_id: int,
        use_case: FromDishka[IGetCompanyDetailUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(company_id=company_id)


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


@router.get(
    "/{company_id}/products",
    response_model=List[ProductRead],
    dependencies=[Depends(get_current_user)]
)
@inject
async def get_products_by_company(
        company_id: int,
        use_case: FromDishka[IProductListByCompanyUseCase],
        name: str = Query(None),
        min_price: float = Query(None),
        max_price: float = Query(None),
        warehouses_id: List[int] = Query([]),
        categories_id: List[int] = Query([]),
):
    return await use_case.execute(
        company_id,
        filters={
            'name': name,
            'min_price': min_price,
            'max_price': max_price,
            'warehouses_id': warehouses_id,
            'categories_id': categories_id,
        }
    )


@router.get(
    "/{company_id}/branches",
    response_model=List[CompanyBranchRead]
)
@inject
async def get_company_branches(
        company_id: int,
        use_case: FromDishka[IGetCompanyBranchesUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(company_id=company_id)
