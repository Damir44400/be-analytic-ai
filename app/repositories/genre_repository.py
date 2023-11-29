from sqlalchemy.orm import Session
from app.models.models import Genre


class GenreRepository:
    def create_genre(self, db: Session, name: str):
        genre = Genre(name=name)
        db.add(genre)
        db.commit()
        return genre

    def get_genres_by_ids(self, db: Session, genre_id_list: list):
        genres = []
        for genre_id in genre_id_list:
            genres.append(
                {"id": self.get_genre_by_id(db, genre_id).id, "genre": self.get_genre_by_id(db, genre_id).name})
        return genres

    def get_genre_by_id(self, db: Session, genre_id: int):
        return db.query(Genre).filter(Genre.id == genre_id).first()

    def get_genre_by_name(self, db: Session, name: str):
        return db.query(Genre).filter(Genre.name == name).first()

    def get_all_genres(self, db: Session):
        return db.query(Genre).all()

    def update_genre(self, db: Session, genre_id: int, new_name: str):
        genre = self.get_genre_by_id(db, genre_id)
        if genre:
            genre.name = new_name
            db.commit()
        return genre

    def delete_genre(self, db: Session, genre_id: int):
        genre = self.get_genre_by_id(db, genre_id)
        if genre:
            db.delete(genre)
            db.commit()
        return genre
