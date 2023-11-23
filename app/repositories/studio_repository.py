from sqlalchemy.orm import Session
from app.models.models import Studio
from app.schemas.studio_schema import StudioCreate, StudioUpdate
from fastapi import HTTPException, status


class StudioRepository:
    @staticmethod
    def get_studio_by_id(db: Session, studio_id: int):
        return db.query(Studio).filter(Studio.id == studio_id).first()

    @staticmethod
    def get_all_studios(db: Session):
        return db.query(Studio).all()

    @staticmethod
    def create_studio(db: Session, studio_create: StudioCreate):
        studio_db = Studio(**studio_create.dict())
        db.add(studio_db)
        db.commit()
        db.refresh(studio_db)
        return studio_db

    @staticmethod
    def update_studio(db: Session, studio_id: int, studio_update: StudioUpdate):
        studio_db = db.query(Studio).filter(Studio.id == studio_id).first()
        if studio_db:
            for key, value in studio_update.dict(exclude_unset=True).items():
                setattr(studio_db, key, value)
            db.commit()
            db.refresh(studio_db)
            return studio_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Studio not found",
            )

    @staticmethod
    def delete_studio(db: Session, studio_id: int):
        studio_db = db.query(Studio).filter(Studio.id == studio_id).first()
        if studio_db:
            db.delete(studio_db)
            db.commit()
            return studio_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Studio not found",
            )
