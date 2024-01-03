from typing import List

from fastapi import Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session

from . import anime_repo, router, genre_repo, genre_anime_repo, category_repo
from app.depends import get_current_user, get_db
from app.schemas.anime_schema import AnimeCreate
from app.utils.media_utils import save_image
from app.schemas.user_schema import UserOut
from .utilits import (
    check_user_privileges,
    check_duplicate_title,
    get_or_create_studio,
)


@router.post("/animes")
async def create_anime_title(
        title: str = Form(...),
        date_announce: int = Form(...),
        country: str = Form(None),
        description: str = Form(...),
        genres: List[str] = Form(...),
        category: str = Form(...),
        studio: str = Form(None),
        cover: UploadFile = File(...),
        db: Session = Depends(get_db),
        user: UserOut = Depends(get_current_user),
):
    try:
        check_user_privileges(user)
        check_duplicate_title(db, title)

        cover = await save_image(cover, cover.filename)
        db_category = category_repo.get_category_by_name(db, category)

        if not db_category:
            raise HTTPException(
                detail="The category not found", status_code=status.HTTP_404_NOT_FOUND
            )

        anime = AnimeCreate(
            title=title,
            cover=cover,
            country=country,
            category_id=db_category.id,
            description=description,
            date_announced=date_announce,
        )

        if studio:
            anime.studio_id = get_or_create_studio(db, studio).id

        db_anime = anime_repo.create_anime(db, anime)

        for genre_name in genres[0].split(','):
            db_genre = genre_repo.get_genre_by_name(db, genre_name)
            if not db_genre:
                raise HTTPException(
                    detail=f"Genre '{genre_name}' not found",
                    status_code=status.HTTP_404_NOT_FOUND,
                )

            genre_anime_repo.create_genre_anime(db, db_genre.id, db_anime.id)
        return {"message": f"The {anime.title} was successfully created"}
    except HTTPException as e:
        raise e
