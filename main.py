import sys, uvicorn, os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers.user_router import router as user_route
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
