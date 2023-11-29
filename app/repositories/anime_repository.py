import datetime

from sqlalchemy.orm import Session
from app.models.models import Anime
from app.schemas.anime_schema import AnimeCreate, AnimeUpdate
from fastapi import HTTPException, status


class AnimeRepository:
    @staticmethod
    def get_anime_by_id(db: Session, anime_id: int):
        return db.query(Anime).filter(Anime.id == anime_id).first()

    @staticmethod
    def get_all_anime(db: Session):
        return db.query(Anime).all()

    @staticmethod
    def create_anime(db: Session, anime_create: AnimeCreate):
        anime_db = Anime(**anime_create.dict())
        db.add(anime_db)
        db.commit()
        db.refresh(anime_db)
        return anime_db

    @staticmethod
    def update_anime(db: Session, anime_id: int, anime_update: AnimeUpdate):
        anime_db = db.query(Anime).filter(Anime.id == anime_id).first()
        if anime_db:
            for key, value in anime_update.dict(exclude_unset=True).items():
                setattr(anime_db, key, value)
            anime_db.date_updated = datetime.datetime.now()
            db.commit()
            db.refresh(anime_db)
            return anime_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Anime not found",
            )

    def delete_anime(self, db: Session, anime_id: int):
        anime_db = self.get_anime_by_id(db, anime_id)
        if anime_db:
            db.delete(anime_db)
            db.commit()
            return anime_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Anime not found",
            )
