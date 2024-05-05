from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.depends import get_db, get_current_user
from app.schemas.company_schema import Company, CompanyCreate
from app.repositories.company_repository import CompanyRepository
from app.schemas.user_schema import User

router = APIRouter()
company_repository = CompanyRepository()


@router.post("/companies/", response_model=Company)
def create_company(company: CompanyCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    inserted = company_repository.create_company(db=db, company=company, user_id=user.id)
    return Company(id=inserted.id, title=inserted.title, description=inserted.description,
                   type_company=inserted.type_company,
                   user_id=user.id)


@router.get("/companies/{company_id}", response_model=Company)
def get_company(company_id: int, user: User = Depends(get_current_user),
                db: Session = Depends(get_db)):
    company = company_repository.get_company_by_id(db=db, company_id=company_id)
    if user is not None and user.id == company.user_id:
        user.is_representative = True
    if company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return Company(id=company.id, title=company.title, description=company.description,
                   type_company=company.type_company,
                   user_id=company.id)


@router.put("/companies/{company_id}")
def update_company(company_id: int, company: CompanyCreate, db: Session = Depends(get_db),
                   user: User = Depends(get_current_user)):
    db_company = company_repository.get_company_by_id(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    elif db_company.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You do not have permission to perform this action")
    updated_company = company_repository.update_company(db=db, company_id=company_id, company_update=company)
    return {"id": updated_company.id}


@router.delete("/companies/{company_id}", response_model=Company)
def delete_company(company_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_company = company_repository.get_company_by_id(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    elif db_company.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You do not have permission to perform this action")
    deleted_company = company_repository.delete_company(db=db, company_id=company_id)
    return {"id": company_id}


@router.get("/companies/", response_model=list[Company])
def get_all_companies(db: Session = Depends(get_db)):
    companies = company_repository.get_all_companies(db=db)
    return [Company(id=company.id, title=company.title, description=company.description,
                    type_company=company.type_company,
                    user_id=company.id) for company in companies]


@router.get("/companies/my/")
def get_all_my_companies(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    companies = company_repository.get_all_companies(db=db)
    return [Company(id=company.id, title=company.title, description=company.description,
                    type_company=company.type_company,
                    user_id=company.user_id) for company in companies if company.user_id == user.id]
