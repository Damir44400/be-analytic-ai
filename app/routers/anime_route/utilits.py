from . import studio_repo, producer_repo, anime_repo
from app.schemas.studio_schema import StudioCreate
from app.schemas.producer_schema import ProducerCreate
from app.schemas.user_schema import UserOut
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def check_user_privileges(user: UserOut):
    if not (user.is_superuser or user.is_moderator):
        raise HTTPException(
            detail="You are not a moderator or superuser",
            status_code=status.HTTP_403_FORBIDDEN
        )


def check_duplicate_title(db: Session, title: str):
    if title.lower() in [anime.title.lower() for anime in anime_repo.get_all_anime(db)]:
        raise HTTPException(
            detail="The title already exists",
            status_code=status.HTTP_400_BAD_REQUEST
        )


def get_or_create_studio(db: Session, studio_name: str):
    db_studio = studio_repo.get_studio_by_name(db, studio_name)
    if not db_studio:
        db_studio = studio_repo.create_studio(db, StudioCreate(name=studio_name))
    return db_studio


def get_or_create_producer(db: Session, producer_name: str):
    db_producer = producer_repo.get_producer_by_name(db, producer_name)
    if not db_producer:
        db_producer = producer_repo.create_producer(db, ProducerCreate(name=producer_name))
    return db_producer
