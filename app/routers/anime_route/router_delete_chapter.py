from . import router, chapter_repo, anime_repo
from fastapi import Depends, HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from ...depends import get_db


@router.delete("/animes/{anime_id}/chapters/{chapter_id}")
async def delete_chapter_detail(anime_id: int, chapter_id: int, db: Session = Depends(get_db)):
    try:
        anime = anime_repo.get_anime_by_id(db, anime_id)
        if anime:
            chapter = chapter_repo.get_anime_chapter_by_id(chapter_id=chapter_id)
            if chapter:
                chapter_repo.delete_anime_chapter(db, chapter_id)
                return {"message": "Chapter successfully deleted"}
            return HTTPException(status_code=404, detail="Not found")
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
