from fastapi import Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import router, user_repo
from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserUpdate, UserOut


@router.patch("/profile", summary="User update")
def user_update(
        data: UserUpdate,
        profile_photo: UploadFile = File(None),
        user: UserOut = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    try:
        print(profile_photo.filename)
        user_repo.update_user(db, user.id, data)
        updated_user = user_repo.get_user_by_id(db, user.id)
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
