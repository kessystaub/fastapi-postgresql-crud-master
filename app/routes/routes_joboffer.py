from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestJoboffer

import crud

router_joboffer = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# joboffer


@router_joboffer.post("/")
async def create_joboffer_service(request: RequestJoboffer, db: Session = Depends(get_db)):
    crud.create_joboffer(db, joboffer=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Joboffer created successfully").dict(exclude_none=True)


@router_joboffer.get("/")
async def get_joboffers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _joboffers = crud.get_joboffer(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_joboffers)


@router_joboffer.get("/names")
async def get_joboffers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _joboffers = crud.get_joboffer(db, skip, limit)
    names = []
    for item in _joboffers:
        names.append(item.name)
    return Response(status="Ok", code="200", message="Success fetch all data", result=names)


@router_joboffer.get("/{joboffer_id}")
async def get_joboffers(joboffer_id: int, db: Session = Depends(get_db)):
    _joboffers = crud.get_joboffer_by_id(db, joboffer_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_joboffers)


@router_joboffer.patch("/{joboffer_id}")
async def update_joboffer(joboffer_id: int, request: RequestJoboffer, db: Session = Depends(get_db)):
    _joboffer = crud.update_joboffer(db, joboffer_id=joboffer_id,
                                     joboffer=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_joboffer)


@router_joboffer.delete("/{joboffer_id}")
async def delete_joboffer(joboffer_id: int,  db: Session = Depends(get_db)):
    crud.remove_joboffer(db, joboffer_id=joboffer_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
