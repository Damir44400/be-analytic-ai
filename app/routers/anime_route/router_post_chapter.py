import os

from . import router, chapter_repo
from fastapi import Depends, HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from ...config import env
from ...depends import get_db, get_current_user
from ...schemas.user_schema import UserOut


@router.post("/animes/{anime_id}/chapters")
async def create_anime_chapter(anime_id: int,
                               anime_video: UploadFile,
                               db: Session = Depends(get_db),
                               user: UserOut = Depends(get_current_user)):
    try:
        if user.is_superuser or user.is_moderator:
            if not is_valid_video(anime_video):
                raise HTTPException(detail="Invalid video format or size", status_code=status.HTTP_400_BAD_REQUEST)

            saved_filename = save_video(anime_video)
            chapter_repo.create_anime_chapter(db, anime_url=saved_filename, anime_id=anime_id)
            return {"message": "Chapter successfully added"}
        else:
            raise HTTPException(detail="You do not have permission to perform this action",
                                status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def is_valid_video(video: UploadFile) -> bool:
    allowed_formats = ["mp4", "avi", "mkv"]
    if not video.filename.split(".")[-1] in allowed_formats:
        return False
    return True


def save_video(video: UploadFile):
    saved_filename = os.path.join(env.VIDEO_PATH, video.filename)
    with open(saved_filename, "wb") as f:
        f.write(video.file.read())

    return saved_filename
