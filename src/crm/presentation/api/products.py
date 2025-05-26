from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends

from src.crm.domain.use_cases.products import (
    IProductCreateUseCase,
    IProductUpdateUseCase,
    IProductDeleteUseCase,
)
from src.crm.presentation.api.depends.authentication import get_current_user
from ..schemas.products import ProductCreate, ProductUpdate, ProductRead
from ...domain.entities.products import ProductEntity
from ...domain.entities.users import UserEntity

router = APIRouter()


@router.post("/", response_model=ProductRead)
@inject
async def create_product(
        form: ProductCreate,
        use_case: FromDishka[IProductCreateUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    product = await use_case.execute(ProductEntity(**form.dict()), auth_user.id)
    return product


@router.patch("/{product_id}", response_model=ProductRead)
@inject
async def update_product(
        product_id: int,
        form: ProductUpdate,
        use_case: FromDishka[IProductUpdateUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(product_id, ProductEntity(**form.dict()), auth_user.id)


@router.delete("/{product_id}", status_code=200)
@inject
async def delete_product(
        product_id: int,
        use_case: FromDishka[IProductDeleteUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(product_id, auth_user.id)
