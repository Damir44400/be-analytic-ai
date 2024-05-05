import json
import secrets
from datetime import datetime, timedelta

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with such email not found")

    try:
        secret_code = ''.join(secrets.choice('0123456789') for _ in range(6))
        sub = {"email": email, "secret_code": secret_code}
        send_email = SendEmail(email, message=secret_code)
        email_result = send_email.send_email()

        if email_result:
            response.set_cookie("code_to_reset", json.dumps(sub), expires=3000,
                                httponly=True, samesite="lax")
            return {"message": "Your password reset code has been sent to your email. Please check your email."}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to send reset code email"
            )
    except HTTPException as e:
        print(e.__class__.__name__)
