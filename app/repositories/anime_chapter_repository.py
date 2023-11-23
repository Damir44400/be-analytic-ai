from sqlalchemy.orm import Session
from app.models.models import AnimeChapter
from app.schemas.anime_schema import AnimeChapterCreate
from fastapi import HTTPException, status


class AnimeChapterRepository:
    @staticmethod
    def create_anime_chapter(db: Session, anime_chapter_create: AnimeChapterCreate):
        anime_chapter_db = AnimeChapter(**anime_chapter_create.dict())
        db.add(anime_chapter_db)
        db.commit()
        db.refresh(anime_chapter_db)
        return anime_chapter_db

    @staticmethod
    def get_anime_chapter_by_id(db: Session, anime_chapter_id: int):
        return db.query(AnimeChapter).filter(AnimeChapter.id == anime_chapter_id).first()

    @staticmethod
    def get_all_anime_chapters(db: Session):
        return db.query(AnimeChapter).all()

    @staticmethod
    def update_anime_chapter(
            db: Session,
            anime_chapter_id: int,
            anime_chapter_update: AnimeChapterCreate
    ):
        anime_chapter_db = db.query(AnimeChapter).filter(AnimeChapter.id == anime_chapter_id).first()

        if anime_chapter_db:
            for key, value in anime_chapter_update.dict(exclude_unset=True).items():
                setattr(anime_chapter_db, key, value)

            db.commit()
            db.refresh(anime_chapter_db)
            return anime_chapter_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Anime Chapter not found",
            )

    @staticmethod
    def delete_anime_chapter(db: Session, anime_chapter_id: int):
        anime_chapter_db = db.query(AnimeChapter).filter(AnimeChapter.id == anime_chapter_id).first()
        if anime_chapter_db:
            db.delete(anime_chapter_db)
            db.commit()
            return anime_chapter_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Anime Chapter not found",
            )
