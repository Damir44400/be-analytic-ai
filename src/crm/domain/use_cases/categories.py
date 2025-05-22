from dataclasses import dataclass
from typing import Optional, Protocol

from src.crm.domain.entities.categories import CategoryEntity


@dataclass
class CategoryForm:
    name: Optional[str] = None
    company_id: Optional[int] = None


class CategoryCreateUseCase(Protocol):

    async def execute(self, body: CategoryForm) -> CategoryEntity:
        ...
