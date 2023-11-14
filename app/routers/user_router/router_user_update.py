from fastapi import Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.utils.security_utils import hash_password
from . import router, user_repo
from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserUpdate, UserOut
from app.utils.media_utils import save_media


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
            filename = await save_media(profile_photo)
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
