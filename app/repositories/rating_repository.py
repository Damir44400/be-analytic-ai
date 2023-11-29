from sqlalchemy.orm import Session
from app.models.models import Rating
from app.schemas.rating_schema import RatingCreate, RatingUpdate


class RatingRepository:
    def create_rating(self, db: Session, rating: RatingCreate, user_id: int):
        rating = Rating(stars=rating.stars, anime_id=rating.anime_id, user_id=user_id)
        db.add(rating)
        db.commit()
        return rating

    def get_rating_by_id(self, db: Session, anime_id: int, user_id: int):
        return db.query(Rating).filter(Rating.anime_id == anime_id and Rating.user_id == user_id).first()

    def get_rating_anime(self, db: Session, anime_id: int):
        return db.query(Rating).filter(Rating.anime_id == anime_id)

    def delete_rating(self, db: Session, rating_id: int, user_id: int):
        rating = self.get_rating_anime(db, rating_id, user_id)
        if rating:
            db.delete(rating)
            db.commit()
        return rating
