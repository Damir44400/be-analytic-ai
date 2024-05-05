from sqlalchemy.orm import Session
from app.models.models import CompanyMachine
from fastapi import HTTPException, status


class CompanyMachineRepository:
    @staticmethod
    def get_machine_by_id(db: Session, machine_id: int):
        return db.query(CompanyMachine).filter(CompanyMachine.id == machine_id).first()

    @staticmethod
    def create_machine(db: Session, train_data: str, company_id: int):
        machine_db = CompanyMachine(train_data=train_data, company_id=company_id)
        db.add(machine_db)
        db.commit()
        db.refresh(machine_db)
        return machine_db

    @staticmethod
    def update_machine(db: Session, machine_id: int, new_train_data: str):
        machine_db = db.query(CompanyMachine).filter(CompanyMachine.id == machine_id).first()
        if machine_db:
            machine_db.train_data = new_train_data
            db.commit()
            db.refresh(machine_db)
            return machine_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Machine not found",
            )

    @staticmethod
    def delete_machine(db: Session, machine_id: int):
        machine_db = db.query(CompanyMachine).filter(CompanyMachine.id == machine_id).first()
        if machine_db:
            db.delete(machine_db)
            db.commit()
            return machine_db
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Machine not found",
            )

    @staticmethod
    def get_all_machines(db: Session):
        return db.query(CompanyMachine).all()
