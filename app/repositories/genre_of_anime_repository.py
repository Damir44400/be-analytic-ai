from sqlalchemy.orm import Session
from app.models.models import GenreAnime
from .genre_repository import GenreRepository


class GenreAnimeRepository:
    def create_genre_anime(self, db: Session, genre_id, anime_id):
        db_genre_anime = GenreAnime(genre_id=genre_id, anime_id=anime_id)
        db.add(db_genre_anime)
        db.commit()
        db.refresh(db_genre_anime)
        return db_genre_anime

    def get_genre_anime_by_anime_id(self, db: Session, anime_id: int):
        return db.query(GenreAnime).filter(GenreAnime.anime_id == anime_id).all()

    def get_genre_anime_from_id(self, db: Session, genre_anime_id: int):
        return db.query(GenreAnime).filter(GenreAnime.id == genre_anime_id).first()

    def get_animes_by_genre(self, db: Session, genre_id: int):
        return db.query(GenreAnime).filter(GenreAnime.genre_id == genre_id).all()

    def get_all_genre_animes(self, db: Session):
        return db.query(GenreAnime).all()

    def delete_anime_genre_by_id(self, db: Session, genre_anime_id: int):
        db_genre_anime = self.get_genre_anime_from_id(db, genre_anime_id)
        if db_genre_anime:
            db.delete(db_genre_anime)
            db.commit()
            return db_genre_anime

    def add_genres_for_anime(self, db: Session, anime_id: int, genres: list):
        db_anime = self.get_genre_anime_by_anime_id(db, anime_id)
        if db_anime:
            genre_repo = GenreRepository()
            for genre_name in genres:
                db_genre = genre_repo.get_genre_by_name(db, genre_name)
                if not db_genre:
                    return False
                self.create_genre_anime(db, db_genre.id, anime_id)
            return True
        return False

    def delete_genre_from_anime(self, db: Session, anime_id: int, anime_genre_id: int):
        db_anime = self.get_genre_anime_by_anime_id(db, anime_id)
        if db_anime:
            db_anime_genre = self.get_genre_anime_from_id(db, anime_genre_id)
            if db_anime_genre:
                self.delete_anime_genre_by_id(db, anime_genre_id)
                return True
            return False
        return False

    def update_genre_on_anime(self, db: Session, anime_id: int, anime_genre_id: int, genre_name: str):
        db_anime = self.get_genre_anime_by_anime_id(db, anime_id)
        if db_anime:
            db_anime_genre = self.get_genre_anime_from_id(db, anime_genre_id)
            if db_anime_genre:
                genre_repo = GenreRepository()
                db_genre = genre_repo.get_genre_by_name(db, genre_name)
                if not db_genre:
                    return False
                db_anime_genre.genre_id = db_genre.id
                db.commit()
                return True
        return False
