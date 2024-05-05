from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.depends import get_db, get_current_user
from app.repositories.train_data_repository import CompanyMachineRepository
from app.repositories.company_repository import CompanyRepository
from app.schemas.train_data_schema import CompanyMachineCreate, CompanyMachineUpdate, CompanyMachine
from app.schemas.user_schema import User

router = APIRouter()
company_machine_repository = CompanyMachineRepository()
company_repository = CompanyRepository()


@router.post("/companies/{company_id}/train_datas", response_model=CompanyMachine)
def create_machine(company_id: int, machine: CompanyMachineCreate, db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    company_db = company_repository.get_company_by_id(db, company_id)
    if company_db.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={})
    machine_db = company_machine_repository.create_machine(db, machine.train_data, user.id)
    return CompanyMachine(id=machine_db.id, company_id=company_db.id, train_data=machine_db.train_data)


@router.get("/companies/{company_id}/train_datas/{machine_id}", response_model=CompanyMachineCreate)
def get_machine(company_id: int, machine_id: int, db: Session = Depends(get_db),
                user: User = Depends(get_current_user)):
    company_db = company_repository.get_company_by_id(db, company_id)
    if company_db.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={})
    machine_db = company_machine_repository.get_machine_by_id(db, machine_id)
    if machine_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Machine not found")
    return CompanyMachine(id=machine_db.id, company_id=company_db.id, train_data=machine_db.train_data)


@router.put("/{machine_id}")
def update_machine(machine_id: int, machine: CompanyMachineUpdate, db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    machine_db = company_machine_repository.get_machine_by_id(db, machine_id)
    company_db = company_repository.get_company_by_id(db, machine_db.company_id)
    if company_db.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={})
    if machine_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Machine not found")
    updated_machine = company_machine_repository.update_machine(db, machine_id, machine.train_data)
    return updated_machine.id


@router.delete("/{machine_id}")
def delete_machine(machine_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    machine_db = company_machine_repository.get_machine_by_id(db, machine_id)
    company_db = company_repository.get_company_by_id(db, machine_db.company_id)
    if company_db.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={})
    if machine_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Machine not found")
    deleted_machine = company_machine_repository.delete_machine(db, machine_id)
    return deleted_machine.id


@router.get("/companies/{company_id}/train_datas", response_model=List[CompanyMachineCreate])
def get_all_machines_of_company(company_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    company_db = company_repository.get_company_by_id(db, company_id)
    if company_db.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={})
    machines = company_machine_repository.get_all_machines(db)
    return [CompanyMachine(id=machine_db.id, company_id=company_db.id, train_data=machine_db.train_data)
            for machine_db in machines]
