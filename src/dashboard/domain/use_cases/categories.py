from dataclasses import dataclass
from typing import Optional, Protocol

from src.dashboard.domain.entities.categories import CategoryEntity


@dataclass
class CategoryForm:
    name: Optional[str]
    company_id: Optional[int]


class CategoryCreateUseCase(Protocol):
    async def execute(self, body: CategoryForm) -> CategoryEntity:
        ...
