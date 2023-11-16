import json
import random
import secrets

from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.depends import get_db
from app.utils.email_utils import SendEmail
from . import router, user_repo
from fastapi import Form, Response, Depends, HTTPException, status


@router.post("/check-email", summary="Reset password if forget")
def check_email(response: Response, email: EmailStr = Form(), db: Session = Depends(get_db)):
    response.delete_cookie("code_to_reset")
    user = user_repo.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not user such email")

    try:
        secret_code = ''.join(secrets.choice('0123456789') for _ in range(6))
        sub = {"email": email, "secret_code": secret_code}
        send_email = SendEmail(email, message=secret_code)
        email_result = send_email.send_email()
        response.set_cookie("code_to_reset", json.dumps(sub), domain=None, expires=100, secure=True, httponly=True,
                            samesite="lax")
        if email_result == "send":
            return {"message": "Your password reset code has been sent to your email. Please check your email."}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to send reset code email"
            )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
