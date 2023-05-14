from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestFormation

import crud

router_formation = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# formation


@router_formation.post("/")
async def create_formation_service(request: RequestFormation, db: Session = Depends(get_db)):
    crud.create_formation(db, formation=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Formation created successfully").dict(exclude_none=True)


@router_formation.get("/")
async def get_formations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _formations = crud.get_formation(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_formations)


@router_formation.get("/{formation_id}")
async def get_formations(formation_id: int, db: Session = Depends(get_db)):
    _formations = crud.get_formation_by_id(db, formation_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_formations)


@router_formation.patch("/{formation_id}")
async def update_formation(formation_id: int, request: RequestFormation, db: Session = Depends(get_db)):
    _formation = crud.update_formation(db, formation_id=formation_id,
                                       formation=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_formation)


@router_formation.delete("/{formation_id}")
async def delete_formation(formation_id: int,  db: Session = Depends(get_db)):
    crud.remove_formation(db, formation_id=formation_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
