from datetime import datetime
from typing import List

from fastapi import Depends, HTTPException, Query, status, UploadFile, File, Form
from sqlalchemy.orm import Session

from . import anime_repo, studio_repo, producer_repo, router, genre_repo, genre_anime_repo
from app.depends import get_current_user, get_db
from app.schemas.anime_schema import AnimeCreate
from app.schemas.user_schema import UserOut
from app.schemas.genre_schema import GenreAnimeCreate
from app.utils.media_utils import save_media
from app.exseptions import raise_not_found_exception


@router.post("/animes")
async def create_anime_title(
        title: str = Form(...),
        date_announce: datetime = Form(None),
        country: str = Form(None),
        description: str = Form(...),
        genre_ids: List[int] = Form(...),
        studio_id: int = Form(None),
        producer_id: int = Form(None),
        cover: UploadFile = File(...),
        db: Session = Depends(get_db),
        user: UserOut = Depends(get_current_user),
):
    if not (user.is_superuser or user.is_moderator):
        raise HTTPException(
            detail="You are not a moderator or superuser",
            status_code=status.HTTP_403_FORBIDDEN
        )

    if title.lower() in [anime.title.lower() for anime in anime_repo.get_all_anime(db)]:
        raise HTTPException(
            detail="The title already exists",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    cover = await save_media(cover, (200, 400))

    if studio_id and not studio_repo.get_studio_by_id(db, studio_id):
        raise_not_found_exception("No studio with that id")

    if producer_id and not producer_repo.get_producer_by_id(db, producer_id):
        raise_not_found_exception("No producer with that id")

    anime = AnimeCreate(
        title=title, cover=cover, date_announce=date_announce, country=country,
        description=description, studio_id=studio_id, producer_id=producer_id
    )
    db_anime = anime_repo.create_anime(db, anime)
    print(genre_ids)
    for genre_id in genre_ids:
        if not genre_repo.get_genre_by_id(db, genre_id):
            raise_not_found_exception("No genre with id {}".format(genre_id))
        genre_anime_repo.create_genre_anime(db, GenreAnimeCreate(genre_id=genre_id, anime_id=db_anime.id))

    return {"message": f"The {anime.title} was successfully created"}