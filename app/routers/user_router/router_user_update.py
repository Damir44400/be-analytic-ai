from fastapi import Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.utils.security_utils import hash_password
from . import router, user_repo
from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserUpdate, UserOut
from app.utils.media_utils import save_image, delete_file


@router.patch("/profile", summary="User update", response_model=UserUpdate)
async def user_update(
        username: str = Form(None),
        email: str = Form(None),
        password: str = Form(None),
        profile_photo: UploadFile = File(None),
        user: UserOut = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    try:
        filename = None
        if profile_photo:
            db_user = user_repo.get_user_by_id(db, user.id)
            delete_file(db_user.profile_photo)
            filename = await save_image(profile_photo, profile_photo.filename)
        if password:
            password = hash_password(password)
        payload = UserUpdate(username=username, email=email, password=password, profile_photo=filename)
        updated_user = user_repo.update_user(db, user.id, payload)
        return UserUpdate(
            username=updated_user.username,
            email=updated_user.email,
            password=updated_user.hashed_password,
            profile_photo=updated_user.profile_photo,
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
