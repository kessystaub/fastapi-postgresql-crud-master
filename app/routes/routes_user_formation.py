from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestUserFormation

import crud

router_user_formation = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# user_formation


@router_user_formation.post("/")
async def create_user_formation_service(request: RequestUserFormation, db: Session = Depends(get_db)):
    crud.create_user_formation(db, user_formation=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="UserFormation created successfully").dict(exclude_none=True)


@router_user_formation.get("/")
async def get_user_formations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _user_formations = crud.get_user_formation(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_formations)


@router_user_formation.get("/{user_formation_id}")
async def get_user_formations(user_formation_id: int, db: Session = Depends(get_db)):
    _user_formations = crud.get_user_formation_by_id(db, user_formation_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_formations)


@router_user_formation.get("/getFormationsByUserId/{user_id}")
async def get_user_formations(user_id: int, db: Session = Depends(get_db)):
    _user_formations = crud.get_formation_by_user_id(db, user_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_formations)


@router_user_formation.patch("/{user_formation_id}")
async def update_user_formation(user_formation_id: int, request: RequestUserFormation, db: Session = Depends(get_db)):
    _user_formation = crud.update_user_formation(db, user_formation_id=user_formation_id,
                                                 user_formation=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_user_formation)


@router_user_formation.delete("/{user_formation_id}")
async def delete_user_formation(user_formation_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_formation(db, user_formation_id=user_formation_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router_user_formation.delete("/deleteByUser/{user_id}/{formation_id}")
async def delete_user_formation(user_id: int, formation_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_formation_by_user(
        db, user_id=user_id, formation_id=formation_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
