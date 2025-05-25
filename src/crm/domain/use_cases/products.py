from typing import Protocol, Dict, List

from src.crm.domain.entities.products import ProductEntity


class IProductCreateUseCase(Protocol):
    async def execute(self, form: ProductEntity, user_id: int) -> ProductEntity:
        ...


class IProductUpdateUseCase(Protocol):
    async def execute(
            self,
            product_id: int,
            form: ProductEntity,
            user_id: int
    ) -> ProductEntity:
        ...


class IProductDeleteUseCase(Protocol):
    async def execute(self, product_id: int, user_id: int) -> Dict[str, str]:
        ...


class IProductListByWarehouseUseCase(Protocol):
    async def execute(self, warehouse_id: int) -> List[ProductEntity]:
        ...


class IProductListByCompanyUseCase(Protocol):
    async def execute(self, company_id: int, filters: ProductEntity) -> List[ProductEntity]:
        ...
