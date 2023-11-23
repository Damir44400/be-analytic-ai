from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.depends import get_db, get_current_user
from app.schemas.user_schema import UserOut
from app.schemas.producer_schema import ProducerUpdate
from . import router, producer_repo


@router.patch("/producers/{producer_id}")
async def update_producers(producer_id: int, producer: ProducerUpdate, db: Session = Depends(get_db),
                           user: UserOut = Depends(get_current_user)):
    if user.is_moderator or user.is_superuser:
        db_producer = producer_repo.get_producer_by_id(db, producer_id)
        if db_producer:
            producer_repo.update_producer(db, producer_id, producer)
            return {"message": f"{db_producer.name} successful updated"}
        return HTTPException(detail="The producer not found", status_code=status.HTTP_404_NOT_FOUND)
    return HTTPException(detail="You are not superuser or moderator", status_code=status.HTTP_403_FORBIDDEN)
