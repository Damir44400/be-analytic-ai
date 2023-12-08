import sys, uvicorn, re, getpass, os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers.user_router import router as user_route
from app.routers.role_router import router as superuser_route
from app.routers.anime_route import router as anime_route
from app.routers.comment_route import router as comment_route
from app.routers.producer_route import router as producer_route
from app.routers.genre_route import router as genre_router
from app.routers.category_route import router as category_route
from app.routers.studio_route import router as studio_router
from app.routers.rating_route import router as rating_router
from app.database import Base, engine
from app.config import fastapi_config, env
from app.repositories.role_repository import RoleRepository

if not os.path.exists("media"):
    os.mkdir("media")
if not os.path.exists("media/images"):
    os.mkdir("media/images")
if not os.path.exists("media/videos"):
    os.mkdir("media/videos")

Base.metadata.create_all(bind=engine)
repository = RoleRepository(engine)
repository.insert_all_roles()

app = FastAPI(**fastapi_config)
app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)
app.include_router(user_route, tags=["User"], prefix="/api/v1")
app.include_router(anime_route, tags=["Anime"], prefix="/api/v1")
app.include_router(comment_route, tags=["Comment"], prefix="/api/v1")
app.include_router(rating_router, tags=['Rating'], prefix="/api/v1")
app.include_router(studio_router, tags=['Studio'], prefix="/api/v1")
app.include_router(category_route, tags=['Category'], prefix="/api/v1")
app.include_router(genre_router, tags=["Genre"], prefix="/api/v1")
app.include_router(producer_route, tags=["Producer"], prefix="/api/v1")
app.include_router(superuser_route, tags=['SuperUser'], prefix='/api/v1')


def main():
    sys_args = sys.argv
    if sys_args[-1] == 'runserver':
        uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    elif sys_args[-1] == 'createsuperuser':
        email = input("Enter email: ")
        email_regex = r'^\S+@\S+\.\S+$'
        while not re.match(email_regex, email):
            print("Invalid email format. Please enter a valid email.")
            email = input("Enter email: ")
        username = input("Enter username: ")
        while not username:
            print("Username cannot be empty.")
            username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        while not password:
            print("Password cannot be empty.")
            password = getpass.getpass("Enter password: ")

        repository.add_super_user(username, email, password)


if __name__ == "__main__":
    main()
