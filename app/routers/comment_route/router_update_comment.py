from . import router, anime_repo, comment_repo
from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.comment_schema import CommentUpdate
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


@router.patch("/animes/{anime_id}/comments/{comment_id}")
async def update_comment(anime_id: int, comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db),
                         user: UserOut = Depends(get_current_user)):
    try:
        db_anime = anime_repo.get_anime_by_id(db, anime_id)
        if db_anime:
            db_comment = comment_repo.check_owner_comment(db, comment_id, user.id)
            if db_comment:
                comment_repo.update_comment_content(db=db, comment_id=comment_id, user_id=user.id,
                                                    new_content=comment.content)
        else:
            raise HTTPException(detail="The anime title not found", status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
