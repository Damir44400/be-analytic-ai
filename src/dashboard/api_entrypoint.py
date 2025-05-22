from fastapi import APIRouter

from .presentation.api.auth import router as auth_router
from .presentation.api.branches import router as branch_router
from .presentation.api.companies import router as company_router
from .presentation.api.users import router as users_router
from .presentation.api.warehouses import router as warehouse_router

router = APIRouter()

router.include_router(company_router, tags=["Companies"], prefix="/companies")
router.include_router(branch_router, tags=["Branches"], prefix="/branches")
router.include_router(warehouse_router, tags=["Warehouses"], prefix="/warehouses")

user_router = APIRouter()

user_router.include_router(auth_router, tags=["Auth"], prefix="/auth")
user_router.include_router(users_router, tags=["Profile"])

router.include_router(user_router, prefix="/users")
