from fastapi import Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.utils.security_utils import hash_password
from . import router, user_repo
from app.depends import get_current_user, get_db
from app.schemas.user_schema import UserCreate, User
from app.utils.media_utils import save_image, delete_file


@router.patch("/profile", summary="User update", response_model=User)
async def user_update(
        username: str = Form(None),
        email: str = Form(None),
        password: str = Form(None),
        user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    try:
        password = hash_password(password)
        payload = UserCreate(username=username, email=email, password=password)
        updated_user = user_repo.update_user(db, user.id, payload)
        return User(id=updated_user.id, username=username, email=email,
                    is_representative=updated_user.is_representative, is_superuser=updated_user.is_superuser)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
