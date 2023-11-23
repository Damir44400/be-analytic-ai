from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.producer_schema import ProducerCreate
from . import router, producer_repo


@router.post("/producers")
async def post_producers(producer: ProducerCreate, db: Session = Depends(get_db),
                         user: UserOut = Depends(get_current_user)):
    if user.is_moderator or user.is_superuser:
        producer_repo.create_producer(db, producer)
        return {"message": f"{producer.name} successful created"}
    return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
