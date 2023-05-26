from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestSoftskill

import crud

router_softskill = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# softskill


@router_softskill.post("/")
async def create_softskill_service(request: RequestSoftskill, db: Session = Depends(get_db)):
    crud.create_softskill(db, softskill=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Softskill created successfully").dict(exclude_none=True)


@router_softskill.get("/")
async def get_softskills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _softskills = crud.get_softskill(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_softskills)


@router_softskill.get("/{softskill_id}")
async def get_softskills(softskill_id: int, db: Session = Depends(get_db)):
    _softskills = crud.get_softskill_by_id(db, softskill_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_softskills)


@router_softskill.get("/getByName/{softskill_name}")
async def get_softskills(softskill_name: str, db: Session = Depends(get_db)):
    _softskills = crud.get_softskill_by_name(db, softskill_name)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_softskills)


@router_softskill.patch("/{softskill_id}")
async def update_softskill(softskill_id: int, request: RequestSoftskill, db: Session = Depends(get_db)):
    _softskill = crud.update_softskill(db, softskill_id=softskill_id,
                                       softskill=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_softskill)


@router_softskill.delete("/{softskill_id}")
async def delete_softskill(softskill_id: int,  db: Session = Depends(get_db)):
    crud.remove_softskill(db, softskill_id=softskill_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
