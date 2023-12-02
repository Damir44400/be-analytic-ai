from typing import List

from . import router, genre_anime_repo, anime_repo, genre_repo
from fastapi import Depends, HTTPException, status, Form
from sqlalchemy.orm import Session

from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserOut

from .utilits import check_user_privileges


@router.post("/animes/{anime_id}/add-genres")
def add_genre_to_anime(anime_id: int, genres: List[str] = Form(None), db: Session = Depends(get_db),
                       user: UserOut = Depends(get_current_user)):
    check_user_privileges(user)
    db_anime = anime_repo.get_anime_by_id(db, anime_id)
    if db_anime:
        if genres:
            for genre in genres:
                db_genre = genre_repo.get_genre_by_name(db, genre)
                if not db_genre:
                    raise HTTPException(detail="Not genre such name", status_code=status.HTTP_404_NOT_FOUND)

            genre_anime_repo.add_genres_for_anime(db, anime_id, genres)
            return {"message": f"The genres {str(genres)} successful added"}

    raise HTTPException(detail="The anime title not found", status_code=status.HTTP_404_NOT_FOUND)
