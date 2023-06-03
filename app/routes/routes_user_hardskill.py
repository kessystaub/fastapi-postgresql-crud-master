from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestUserHardskill

import crud

router_user_hardskill = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# user_hardskill


@router_user_hardskill.post("/")
async def create_user_hardskill_service(request: RequestUserHardskill, db: Session = Depends(get_db)):
    crud.create_user_hardskill(db, user_hardskill=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="UserHardskill created successfully").dict(exclude_none=True)


@router_user_hardskill.get("/")
async def get_user_hardskills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _user_hardskills = crud.get_user_hardskill(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_hardskills)


@router_user_hardskill.get("/{user_hardskill_id}")
async def get_user_hardskills(user_hardskill_id: int, db: Session = Depends(get_db)):
    _user_hardskills = crud.get_user_hardskill_by_id(db, user_hardskill_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_hardskills)


@router_user_hardskill.get("/getHardskillsByUserId/{user_id}")
async def get_user_hardskills(user_id: int, db: Session = Depends(get_db)):
    _user_hardskills = crud.get_hardskill_by_user_id(db, user_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_hardskills)


@router_user_hardskill.get("/getHardskillsByUserId2/{user_id}")
async def get_user_hardskills(user_id: int, db: Session = Depends(get_db)):
    _user_hardskills = crud.get_hardskill_by_user_id2(db, user_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_hardskills)


@router_user_hardskill.patch("/{user_hardskill_id}")
async def update_user_hardskill(user_hardskill_id: int, request: RequestUserHardskill, db: Session = Depends(get_db)):
    _user_hardskill = crud.update_user_hardskill(db, user_hardskill_id=user_hardskill_id,
                                                 user_hardskill=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_user_hardskill)


@router_user_hardskill.get("/getByUserAndHardkill/{user_id}/{hardskill_id}")
async def get_user_hardskills(user_id: int, hardskill_id: int, db: Session = Depends(get_db)):
    _user_hardskills = crud.get_user_hardskill_by_hardskill_id(
        db, user_id, hardskill_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_hardskills)


@router_user_hardskill.delete("/{user_hardskill_id}")
async def delete_user_hardskill(user_hardskill_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_hardskill(db, user_hardskill_id=user_hardskill_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router_user_hardskill.delete("/deleteByUser/{user_id}/{hardskill_id}")
async def delete_user_hardskill(user_id: int, hardskill_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_hardskill_by_user(
        db, user_id=user_id, hardskill_id=hardskill_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
