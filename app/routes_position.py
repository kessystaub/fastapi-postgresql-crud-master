from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestPosition

import crud

router_position = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# position


@router_position.post("/")
async def create_position_service(request: RequestPosition, db: Session = Depends(get_db)):
    crud.create_position(db, position=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Position created successfully").dict(exclude_none=True)


@router_position.get("/")
async def get_positions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _positions = crud.get_position(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_positions)


@router_position.get("/{position_id}")
async def get_positions(position_id: int, db: Session = Depends(get_db)):
    _positions = crud.get_position_by_id(db, position_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_positions)


@router_position.patch("/{position_id}")
async def update_position(position_id: int, request: RequestPosition, db: Session = Depends(get_db)):
    _position = crud.update_position(db, position_id=position_id,
                                     position=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_position)


@router_position.delete("/{position_id}")
async def delete_position(position_id: int,  db: Session = Depends(get_db)):
    crud.remove_position(db, position_id=position_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
