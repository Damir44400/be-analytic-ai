from sqlalchemy.orm import Session
from app.models.models import Producer
from app.schemas.producer_schema import ProducerCreate, ProducerUpdate
from fastapi import HTTPException, status


class ProducerRepository:
    @staticmethod
    def get_producer_by_id(db: Session, producer_id: int):
        return db.query(Producer).filter(Producer.id == producer_id).first()

    @staticmethod
    def get_all_producers(db: Session):
        return db.query(Producer).all()

    @staticmethod
    def create_producer(db: Session, producer_create: ProducerCreate):
        producer_db = Producer(**producer_create.dict())
        db.add(producer_db)
        db.commit()
        db.refresh(producer_db)
        return producer_db

    @staticmethod
    def update_producer(db: Session, producer_id: int, producer_update: ProducerUpdate):
        producer_db = db.query(Producer).filter(Producer.id == producer_id).first()
        if producer_db:
            for key, value in producer_update.dict(exclude_unset=True).items():
                setattr(producer_db, key, value)
            db.commit()
            db.refresh(producer_db)
            return producer_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producer not found",
            )

    @staticmethod
    def delete_producer(db: Session, producer_id: int):
        producer_db = db.query(Producer).filter(Producer.id == producer_id).first()
        if producer_db:
            db.delete(producer_db)
            db.commit()
            return producer_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producer not found",
            )
