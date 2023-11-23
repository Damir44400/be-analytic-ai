from sqlalchemy.orm import Session

from app.models.models import GenreAnime


class GenreAnimeRepository:
    def create_genre_anime(self, db: Session, genre_anime_create):
        db_genre_anime = GenreAnime(**genre_anime_create.dict())
        db.add(db_genre_anime)
        db.commit()
        db.refresh(db_genre_anime)
        return db_genre_anime

    def get_genre_anime_by_id(self, db: Session, genre_anime_id: int):
        return db.query(GenreAnime).filter(GenreAnime.id == genre_anime_id).first()

    def get_genre_animes(self, db: Session):
        return db.query(GenreAnime).all()

    def update_genre_anime(self, db: Session, genre_anime_id: int, genre_anime_update):
        db_genre_anime = self.get_genre_anime_by_id(db, genre_anime_id)
        if db_genre_anime:
            for key, value in genre_anime_update.dict().items():
                setattr(db_genre_anime, key, value)
            db.commit()
            db.refresh(db_genre_anime)
        return db_genre_anime

    def delete_genre_anime(self, db: Session, genre_anime_id: int):
        db_genre_anime = self.get_genre_anime_by_id(db, genre_anime_id)
        if db_genre_anime:
            db.delete(db_genre_anime)
            db.commit()

        return db_genre_anime
