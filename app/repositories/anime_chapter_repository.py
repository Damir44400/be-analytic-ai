from sqlalchemy.orm import Session
from app.models.models import AnimeChapter
from app.schemas.anime_schema import AnimeChapterCreate
from fastapi import HTTPException, status


class AnimeChapterRepository:
    def create_anime_chapter(self, db: Session, anime_url: str, anime_id: int):
        anime_chapter = len(self.get_anime_chapter_by_id(db, anime_id)) + 1
        anime_chapter_db = AnimeChapter(anime_video_url=anime_url, chapter=anime_chapter, anime_id=anime_id)
        db.add(anime_chapter_db)
        db.commit()
        db.refresh(anime_chapter_db)
        return anime_chapter_db

    @staticmethod
    def get_anime_chapter_by_id(db: Session, chapter_id: int):
        return db.query(AnimeChapter).filter(AnimeChapter.id == chapter_id).first()

    @staticmethod
    def get_all_anime_chapters(db: Session, anime_id: int):
        return db.query(AnimeChapter).filter(AnimeChapter.anime_id == anime_id).all()

    @staticmethod
    def update_anime_chapter(
            db: Session,
            anime_chapter_id: int,
            anime_url: str,
            chapter: int
    ):
        anime_chapter_db = db.query(AnimeChapter).filter(AnimeChapter.id == anime_chapter_id).first()

        if anime_chapter_db:
            anime_chapter_db.anime_video_url = anime_url
            anime_chapter_db.chapter = chapter
            db.commit()
            db.refresh(anime_chapter_db)
            return anime_chapter_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Anime Chapter not found",
            )

    @staticmethod
    def delete_anime_chapter(db: Session, chapter_id: int):
        anime_chapter_db = db.query(AnimeChapter).filter(AnimeChapter.id == chapter_id).first()
        if anime_chapter_db:
            db.delete(anime_chapter_db)
            db.commit()
            return anime_chapter_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Anime Chapter not found",
            )
