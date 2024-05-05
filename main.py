import sys, uvicorn, os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers.user_router import router as user_route
from app.routers.company_router.router_company import router as company_route
from app.routers.company_router.router_train_data import router as machine_router
from app.routers.router_spech_to_text import router as speech_router
from app.database import Base, engine
from app.config import fastapi_config, env

Base.metadata.create_all(bind=engine)

app = FastAPI(**fastapi_config)
app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)

app.include_router(user_route, tags=["User"], prefix="/api/v1")
app.include_router(company_route, tags=["Company"], prefix="/api/v1")
app.include_router(machine_router, tags=["Machine"], prefix="/api/v1")
app.include_router(speech_router, tags=["Speech"], prefix="/api/v1")