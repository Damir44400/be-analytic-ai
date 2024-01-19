from . import router, chapter_repo, anime_repo
from fastapi import Depends, HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from ...depends import get_db


@router.put("/animes/{anime_id}/chapters/{chapter_id}")
async def update_anime_chapter(
        anime_id: int,
        chapter_id: int,
        anime_url: str,
        chapter_number: int,
        db: Session = Depends(get_db)
):
    try:
        anime = anime_repo.get_anime_by_id(db, anime_id)
        if anime:
            chapter = chapter_repo.get_anime_chapter_by_id(db, chapter_id)
            if chapter:
                updated_chapter = chapter_repo.update_anime_chapter(
                    db,
                    chapter_id=chapter_id,
                    anime_url=anime_url,
                    chapter=chapter_number
                )
                return {"message": "Chapter successfully updated", "updated_chapter": updated_chapter}
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found")
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
