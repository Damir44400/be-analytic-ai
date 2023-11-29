from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.models import AnimeDateCreated


class AnimeDateCreatedRepository:
    def create_anime_date(self, db: Session, release_date: int):
        anime_date = AnimeDateCreated(year=release_date)
        db.add(anime_date)
        try:
            db.commit()
            db.refresh(anime_date)
            return anime_date
        except IntegrityError:
            db.rollback()
            return None

    def get_anime_date_by_id(self, db: Session, anime_date_id: int):
        return db.query(AnimeDateCreated).filter(AnimeDateCreated.id == anime_date_id).first()

    def get_anime_date_by_release_date(self, db: Session, release_date: int):
        return db.query(AnimeDateCreated).filter(AnimeDateCreated.year == release_date).first()

    def update_anime_date(self, db: Session, anime_date_id: int, new_release_date: int):
        anime_date = self.get_anime_date_by_id(db, anime_date_id)
        if anime_date:
            anime_date.year = new_release_date
            db.commit()
            db.refresh(anime_date)
            return anime_date
        return None

    def delete_anime_date(self, db: Session, anime_date_id: int):
        anime_date = self.get_anime_date_by_id(db, anime_date_id)
        if anime_date:
            db.delete(anime_date)
            db.commit()
            return True
        return False

    def get_all_announce_dates(self, db: Session):
        return db.query(AnimeDateCreated).all()
