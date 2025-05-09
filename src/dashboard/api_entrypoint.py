from fastapi import APIRouter

from .presentation.api.companies import router as company_router

router = APIRouter(prefix="/companies")

router.include_router(company_router, tags=["Companies"])
