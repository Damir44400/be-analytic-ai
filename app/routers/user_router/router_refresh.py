import json
from . import router, user_repo

from fastapi import Response, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.utils.jwt_utils import create_access_token, validate_date_token, decode_token
from app.config import env
from app.depends import get_db


@router.post("/sign-in/refresh-token")
async def token_refresh(response: Response, refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = decode_token(token=refresh_token, key=env.JWT_REFRESH_SECRET_KEY)
        if not validate_date_token(payload):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not payload["sub"]:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not refresh access token')

        payload_str = str(payload["sub"]).replace("'", "\"")
        payload_dict = json.loads(payload_str)
        user = user_repo.get_user_by_username(db, payload_dict["username"])
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='The user belonging to this token no longer exists')

        access_token = create_access_token({"user_id": user.id, "username": user.username})
    except Exception as e:
        error = e.__class__.__name__
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='Please provide refresh token')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    response.set_cookie('access_token', access_token, env.ACCESS_TOKEN_EXPIRE_MINUTES,
                        env.ACCESS_TOKEN_EXPIRE_MINUTES, '/', None, False, True, 'lax')
    response.set_cookie('logged_in', 'True', env.ACCESS_TOKEN_EXPIRE_MINUTES,
                        env.ACCESS_TOKEN_EXPIRE_MINUTES, '/', None, False, False, 'lax')
    return {'access_token': access_token}
