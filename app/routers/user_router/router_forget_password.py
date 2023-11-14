import json

from sqlalchemy.orm import Session

from app.depends import get_db
from . import router, user_repo
from fastapi import Form, Request, HTTPException, status, Depends, Response
from app.utils.security_utils import hash_password


@router.patch("/reset-password", summary="Reset password if forget")
def reset_password(request: Request, response: Response, code: str = Form(), new_password: str = Form(),
                   db: Session = Depends(get_db)):
    if not request.cookies.get("code_to_reset"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The code expire time passed"
        )
    cookie = json.loads(request.cookies.get('code_to_reset'))
    cookie_code = cookie["secret_code"]
    if code != cookie_code:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect code")
    response.delete_cookie('code_to_reset')
    user_repo.reset_password(db, cookie["email"], hash_password(new_password))
    return {"message", "Successful reset"}
