from src.core.domain.interfaces import IUoW
from src.core.exceptions import BadRequestException
from src.crm.domain.entities.categories import CategoryEntity
from src.crm.domain.interfaces.daos.categories import ICategoryCreateDAO, ICategoryGetByNameCompanyDAO
from src.crm.domain.use_cases.categories import CategoryForm


class CategoryGateway(
    ICategoryCreateDAO,
    ICategoryGetByNameCompanyDAO
):
    ...


class CreateCategoryUseCase:
    def __init__(
            self,
            uow: IUoW,
            category_gateway: CategoryGateway
    ):
        self._uow = uow
        self._category_gateway = category_gateway

    async def execute(self, body: CategoryForm) -> CategoryEntity:
        db_category = await self._category_gateway.get_by_name(body.name, body.company_id)
        if db_category:
            raise BadRequestException("Category already exists with this given name")

        async with self._uow:
            await self._category_gateway.create(
                CategoryEntity(
                    name=body.name,
                    company_id=body.company_id
                )
            )
        return db_category
