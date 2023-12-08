from . import router, rating_repo, anime_repo
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.rating_schema import RatingCreate

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


@router.post("/rating/{anime_id}")
async def put_rating(
        rating: RatingCreate,
        db: Session = Depends(get_db),
        user: UserOut = Depends(get_current_user)
):
    try:
        anime = anime_repo.get_anime_by_id(db, rating.anime_id)
        if anime:
            existing_rating = rating_repo.check_exists_rating_for_anime(db, anime_id=rating.anime_id, user_id=user.id)
            if not existing_rating:
                db_rating = rating_repo.create_rating(db, rating, user_id=user.id)
                return {"message": db_rating.stars}
            else:
                return {"message": "You have already submitted a rating for this title"}
        else:
            raise HTTPException(detail="No anime found with the provided id", status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail=f"Internal server error: {str(e)}",
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
