from . import router
from fastapi import status, Response, Depends
from app.depends import get_current_user
from ...schemas.user_schema import User


@router.get('/logout', status_code=status.HTTP_200_OK)
async def logout(response: Response, user: User = Depends(get_current_user)):
    response.delete_cookie("access_token")
    response.set_cookie('logged_in', '', -1)

    return {'status': 'success'}
