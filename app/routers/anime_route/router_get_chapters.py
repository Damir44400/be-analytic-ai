from . import router, chapter_repo, anime_repo
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...depends import get_db, get_current_user


@router.get("/animes/{anime_id}/chapters")
async def get_anime_chapters(anime_id: int, db: Session = Depends(get_db)):
    try:
        anime = anime_repo.get_anime_by_id(db, anime_id)
        if not anime:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Anime with ID {anime_id} not found")

        chapters = chapter_repo.get_all_anime_chapters(db, anime_id=anime_id)
        return chapters
    except Exception as e:
        print(e)
        raise HTTPException(detail="Internal Server Error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
