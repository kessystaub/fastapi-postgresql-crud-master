from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestCompany

import crud

router_company = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# company


@router_company.post("/")
async def create_company_service(request: RequestCompany, db: Session = Depends(get_db)):
    crud.create_company(db, company=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Company created successfully").dict(exclude_none=True)


@router_company.get("/")
async def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _companies = crud.get_company(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_companies)


@router_company.get("/{company_id}")
async def get_companies(company_id: int, db: Session = Depends(get_db)):
    _companies = crud.get_company_by_id(db, company_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_companies)


@router_company.patch("/{company_id}")
async def update_company(company_id: int, request: RequestCompany, db: Session = Depends(get_db)):
    _company = crud.update_company(db, company_id=company_id,
                                   company=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_company)


@router_company.delete("/{company_id}")
async def delete_company(company_id: int,  db: Session = Depends(get_db)):
    crud.remove_company(db, company_id=company_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
