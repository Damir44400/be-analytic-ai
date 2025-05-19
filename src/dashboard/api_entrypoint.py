from fastapi import APIRouter

from .presentation.api.branches import router as branch_router
from .presentation.api.companies import router as company_router
from .presentation.api.warehouses import router as warehouse_router

router = APIRouter()

router.include_router(company_router, tags=["Companies"], prefix="/companies")
router.include_router(branch_router, tags=["Branches"], prefix="/branches")
router.include_router(warehouse_router, tags=["Warehouses"], prefix="/warehouses")
