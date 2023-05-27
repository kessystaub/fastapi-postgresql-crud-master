from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestInstitution

import crud

router_institution = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# institution


@router_institution.post("/")
async def create_institution_service(request: RequestInstitution, db: Session = Depends(get_db)):
    crud.create_institution(db, institution=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Institution created successfully").dict(exclude_none=True)


@router_institution.get("/")
async def get_institutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _institutions = crud.get_institution(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_institutions)


@router_institution.get("/getByName/{institution_name}")
async def get_institutions(institution_name: str, db: Session = Depends(get_db)):
    _institutions = crud.get_institution_by_name(db, institution_name)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_institutions)


@router_institution.get("/{institution_id}")
async def get_institutions(institution_id: int, db: Session = Depends(get_db)):
    _institutions = crud.get_institution_by_id(db, institution_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_institutions)


@router_institution.patch("/{institution_id}")
async def update_institution(institution_id: int, request: RequestInstitution, db: Session = Depends(get_db)):
    _institution = crud.update_institution(db, institution_id=institution_id,
                                           institution=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_institution)


@router_institution.delete("/{institution_id}")
async def delete_institution(institution_id: int,  db: Session = Depends(get_db)):
    crud.remove_institution(db, institution_id=institution_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
