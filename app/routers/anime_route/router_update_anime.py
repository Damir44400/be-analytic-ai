from typing import List

from fastapi import Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session

from . import anime_repo, router, genre_repo, genre_anime_repo, announce_repo, category_repo
from app.depends import get_current_user, get_db
from app.schemas.anime_schema import AnimeUpdate
from app.utils.media_utils import save_media
from app.schemas.user_schema import UserOut
from .utilits import (
    check_user_privileges,
    check_duplicate_title,
    get_or_create_studio,
    get_or_create_producer
)


@router.patch("/animes/{anime_id}")
async def create_anime_title(
        anime_id: int,
        title: str = Form(None),
        date_announce: int = Form(None),
        country: str = Form(None),
        description: str = Form(None),
        category: str = Form(None),
        studio: str = Form(None),
        producer: str = Form(None),
        cover: UploadFile = File(None),
        db: Session = Depends(get_db),
        user: UserOut = Depends(get_current_user),
):
    try:
        check_user_privileges(user)
        anime_db = anime_repo.get_anime_by_id(db, anime_id)
        if not anime_db:
            raise HTTPException(detail="The anime title not found", status_code=status.HTTP_404_NOT_FOUND)

        if title and title != anime_db.title:
            check_duplicate_title(db, title)

        anime = AnimeUpdate(
            title=title or anime_db.title,
            cover=await save_media(cover, (200, 340)) if cover else anime_db.cover,
            date_announce=date_announce or anime_db.date_announce,
            description=description or anime_db.description,
            country=country or anime_db.country,
            studio_id=get_or_create_studio(db, studio).id if studio else anime_db.studio_id,
            producer_id=get_or_create_producer(db, producer).id if producer else anime_db.producer_id,
            category_id=category_repo.get_category_by_name(db, category).id if category else anime_db.category_id,
        )

        db_anime = anime_repo.update_anime(db, anime_id, anime)

        return {"message": f"The {db_anime.title} was successfully updated"}
    except HTTPException as e:
        raise e
