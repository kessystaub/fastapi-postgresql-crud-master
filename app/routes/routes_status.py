from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestStatus

import crud

router_status = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# status


@router_status.post("/")
async def create_status_service(request: RequestStatus, db: Session = Depends(get_db)):
    crud.create_status(db, status=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Status created successfully").dict(exclude_none=True)


@router_status.get("/")
async def get_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _statuses = crud.get_status(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_statuses)


@router_status.get("/{status_id}")
async def get_statuses(status_id: int, db: Session = Depends(get_db)):
    _statuses = crud.get_status_by_id(db, status_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_statuses)


@router_status.patch("/{status_id}")
async def update_status(status_id: int, request: RequestStatus, db: Session = Depends(get_db)):
    _status = crud.update_status(db, status_id=status_id,
                                 status=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_status)


@router_status.delete("/{status_id}")
async def delete_status(status_id: int,  db: Session = Depends(get_db)):
    crud.remove_status(db, status_id=status_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
