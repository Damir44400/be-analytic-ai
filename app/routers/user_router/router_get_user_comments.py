from . import router, comment_repo, anime_repo
from sqlalchemy.orm import Session
from app.depends import get_db
from fastapi import HTTPException, Depends, status


@router.get("/users/get-user/{user_id}/comments")
async def get_user_comments(user_id: int, db: Session = Depends(get_db)):
    try:
        db_comments = comment_repo.get_comments_by_user_id(db, user_id)
        comments = []
        for comment in db_comments:
            print(comment.anime_id)
            tmp_comment = {
                "anime": {
                    "id": comment.anime_id,
                    "title": anime_repo.get_anime_by_id(db, comment.anime_id).title
                },
                "content": comment_repo.get_comment_by_id(db, comment.id).content,
                "date_upload": comment_repo.get_comment_by_id(db, comment.id).date_uploaded
            }
            comments.append(tmp_comment)
        return comments
    except Exception as e:
        print(e)
        raise HTTPException(detail="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
