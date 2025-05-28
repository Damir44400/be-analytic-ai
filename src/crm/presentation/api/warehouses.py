from typing import List

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends

from src.crm.domain.use_cases.warehouses import (
    IWarehouseCreateUseCase,
    IWarehouseUpdateUseCase,
    IWarehouseDeleteUseCase,
    IGetWarehouseProductsUseCase
)
from src.crm.presentation.api.depends.authentication import get_current_user
from ..schemas.products import ProductRead
from ..schemas.warehouses import (
    WarehouseCreate,
    WarehouseRead,
    WarehouseUpdate
)
from ...domain.entities.users import UserEntity
from ...domain.entities.warehouse import WarehouseEntity

router = APIRouter()


@router.post("/", response_model=WarehouseRead, responses={
    200: {
        "content": {
            "application/json": {
                "example": {
                    "detail": "Successfully created warehouse"
                }
            }
        }
    }
})
@inject
async def create_warehouse(
        form: WarehouseCreate,
        use_case: FromDishka[IWarehouseCreateUseCase],
        auth_user: UserEntity = Depends(get_current_user)):
    return await use_case.execute(WarehouseEntity(**form.dict()), auth_user.id)


@router.patch("/{warehouse_id}", response_model=WarehouseRead)
@inject
async def update_warehouse(
        warehouse_id: int,
        form: WarehouseUpdate,
        use_case: FromDishka[IWarehouseUpdateUseCase],
        auth_user: UserEntity = Depends(get_current_user)
):
    return await use_case.execute(warehouse_id, auth_user.id, WarehouseEntity(**form.dict()))


@router.delete("/{warehouse_id}", status_code=200)
@inject
async def delete_warehouse(
        warehouse_id: int,
        use_case: FromDishka[IWarehouseDeleteUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(warehouse_id, auth_user.id)


@router.get("/{warehouse_id}/products", response_model=List[ProductRead])
@inject
async def get_warehouses_for_product(
        warehouse_id: int,
        use_case: FromDishka[IGetWarehouseProductsUseCase],
        auth_user: UserEntity = Depends(get_current_user),
):
    return await use_case.execute(warehouse_id)
