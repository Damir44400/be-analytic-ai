from . import router, chapter_repo, anime_repo
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...depends import get_db


@router.get("/animes/{anime_id}/chapters/{chapter_id}")
async def get_chapter_detail(anime_id: int, chapter_id: int, db: Session = Depends(get_db)):
    try:
        anime = anime_repo.get_anime_by_id(db, anime_id)
        if anime:
            chapter = chapter_repo.get_anime_chapter_by_id(db, chapter_id)
            if chapter:
                return chapter
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found")
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
