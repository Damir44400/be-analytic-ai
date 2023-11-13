from fastapi import FastAPI
from app.routing.user_route import router as user_route
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route)
