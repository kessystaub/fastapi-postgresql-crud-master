from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestHardskill

import crud

router_hardskill = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# hardskill


@router_hardskill.post("/")
async def create_hardskill_service(request: RequestHardskill, db: Session = Depends(get_db)):
    crud.create_hardskill(db, hardskill=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Hardskill created successfully").dict(exclude_none=True)


@router_hardskill.get("/")
async def get_hardskills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _hardskills = crud.get_hardskill(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_hardskills)


@router_hardskill.get("/{hardskill_id}")
async def get_hardskills(hardskill_id: int, db: Session = Depends(get_db)):
    _hardskills = crud.get_hardskill_by_id(db, hardskill_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_hardskills)


@router_hardskill.get("/getByName/{hardskill_name}")
async def get_hardskills(hardskill_name: str, db: Session = Depends(get_db)):
    _hardskills = crud.get_hardskill_by_name(db, hardskill_name)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_hardskills)


@router_hardskill.patch("/{hardskill_id}")
async def update_hardskill(hardskill_id: int, request: RequestHardskill, db: Session = Depends(get_db)):
    _hardskill = crud.update_hardskill(db, hardskill_id=hardskill_id,
                                       hardskill=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_hardskill)


@router_hardskill.delete("/{hardskill_id}")
async def delete_hardskill(hardskill_id: int,  db: Session = Depends(get_db)):
    crud.remove_hardskill(db, hardskill_id=hardskill_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
