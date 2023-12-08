from . import router, genre_anime_repo, genre_repo, anime_repo
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from .utilits import check_user_privileges


@router.delete("/animes/{anime_id}/genres/{genre_id}")
def delete_genre_from_anime(anime_id: int, genre_id: int, db: Session = Depends(get_db),
                            user: UserOut = Depends(get_current_user)):
    try:
        check_user_privileges(user)
        anime_title = anime_repo.get_anime_by_id(db, anime_id)
        print(anime_title.title)
        genres = genre_anime_repo.get_genre_anime_by_anime_id(db, anime_id)
        if genres:
            for genre in genres:
                if genre.genre_id == genre_id:
                    genre_anime_repo.delete_genre_from_anime(db, anime_id, genre_id)
                    genre_name = genre_repo.get_genre_by_id(db, genre_id).name
                    return {"message": f"{genre_name} successfully deleted from title {anime_title}"}
            raise HTTPException(
                detail=f"The {genre_repo.get_genre_by_id(db, genre_id).name} not found from title {anime_title}",
                status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(detail=f"The title {anime_title} not found",
                            status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e.__class__.__name__)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
