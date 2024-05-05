from sqlalchemy.orm import Session
from app.models.models import Company
from app.schemas.company_schema import CompanyCreate
from fastapi import HTTPException, status


class CompanyRepository:
    @staticmethod
    def get_company_by_id(db: Session, company_id: int):
        return db.query(Company).filter(Company.id == company_id).first()

    @staticmethod
    def create_company(db: Session, company: CompanyCreate, user_id: int):
        company_db = Company(**company.dict(), user_id=user_id)
        db.add(company_db)
        db.commit()
        db.refresh(company_db)
        return company_db

    @staticmethod
    def update_company(db: Session, company_id: int, company_update: CompanyCreate):
        company_db = db.query(Company).filter(Company.id == company_id).first()
        if company_db:
            for field, value in company_update.dict().items():
                setattr(company_db, field, value)
            db.commit()
            db.refresh(company_db)
            return company_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found",
            )

    @staticmethod
    def delete_company(db: Session, company_id: int):
        company_db = db.query(Company).filter(Company.id == company_id).first()
        if company_db:
            db.delete(company_db)
            db.commit()
            return company_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found",
            )

    @staticmethod
    def get_all_companies(db: Session):
        return db.query(Company).all()
