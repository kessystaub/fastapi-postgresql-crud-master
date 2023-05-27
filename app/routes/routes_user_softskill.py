from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestUserSoftskill

import crud

router_user_softskill = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# user_softskill


@router_user_softskill.post("/")
async def create_user_softskill_service(request: RequestUserSoftskill, db: Session = Depends(get_db)):
    crud.create_user_softskill(db, user_softskill=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="UserSoftskill created successfully").dict(exclude_none=True)


@router_user_softskill.get("/")
async def get_user_softskills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _user_softskills = crud.get_user_softskill(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_softskills)


@router_user_softskill.get("/{user_softskill_id}")
async def get_user_softskills(user_softskill_id: int, db: Session = Depends(get_db)):
    _user_softskills = crud.get_user_softskill_by_id(db, user_softskill_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_softskills)


@router_user_softskill.get("/getSoftskillsByUserId/{user_id}")
async def get_user_softskills(user_id: int, db: Session = Depends(get_db)):
    _user_softskills = crud.get_softskill_by_user_id(db, user_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_softskills)


@router_user_softskill.patch("/{user_softskill_id}")
async def update_user_softskill(user_softskill_id: int, request: RequestUserSoftskill, db: Session = Depends(get_db)):
    _user_softskill = crud.update_user_softskill(db, user_softskill_id=user_softskill_id,
                                                 user_softskill=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_user_softskill)


@router_user_softskill.delete("/{user_softskill_id}")
async def delete_user_softskill(user_softskill_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_softskill(db, user_softskill_id=user_softskill_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router_user_softskill.get("/getByUserAndSoftskill/{user_id}/{softskill_id}")
async def get_user_softskills(user_id: int, softskill_id: int, db: Session = Depends(get_db)):
    _user_softskills = crud.get_user_softskill_by_softskill_id(
        db, user_id, softskill_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_softskills)


@router_user_softskill.delete("/deleteByUser/{user_id}/{softskill_id}")
async def delete_user_softskill(user_id: int, softskill_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_softskill_by_user(
        db, user_id=user_id, softskill_id=softskill_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
