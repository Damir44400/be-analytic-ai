from . import router, anime_repo, comment_repo
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.comment_schema import CommentCreate
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


@router.post("/animes/{anime_id}/comments")
async def create_comment(anime_id: int, comment: CommentCreate, db: Session = Depends(get_db),
                         user: UserOut = Depends(get_current_user)):
    try:
        db_anime = anime_repo.get_anime_by_id(db, anime_id)
        if db_anime:
            comment_repo.create_comment(db, comment.content, user.id, anime_id)
            return {"message": f"{comment.content}"}
        else:
            raise HTTPException(detail="The anime title not found", status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
