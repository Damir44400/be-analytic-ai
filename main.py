from fastapi import FastAPI
from app.routers.user_router import router as user_route
from app.database import Base, engine
from app.config import fastapi_config

Base.metadata.create_all(bind=engine)

app = FastAPI(**fastapi_config)
app.include_router(user_route, tags=["User"],prefix="/api")
