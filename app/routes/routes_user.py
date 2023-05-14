from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, RequestCity, RequestUser

import crud

router_user = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# user


@router_user.post("/")
async def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="User created successfully").dict(exclude_none=True)


@router_user.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@router_user.get("/{user_id}")
async def get_users(user_id: int, db: Session = Depends(get_db)):
    _users = crud.get_user_by_id(db, user_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@router_user.patch("/{user_id}")
async def update_user(user_id: int, request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.update_user(db, user_id=user_id,
                             user=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_user)


@router_user.delete("/{user_id}")
async def delete_user(user_id: int,  db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=user_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)