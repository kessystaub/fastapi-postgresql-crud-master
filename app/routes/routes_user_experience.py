from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestUserExperience

import crud

router_user_experience = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# user_experience


@router_user_experience.post("/")
async def create_user_experience_service(request: RequestUserExperience, db: Session = Depends(get_db)):
    crud.create_user_experience(db, user_experience=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="UserExperience created successfully").dict(exclude_none=True)


@router_user_experience.get("/")
async def get_user_experiences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _user_experiences = crud.get_user_experience(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_experiences)


@router_user_experience.get("/{user_experience_id}")
async def get_user_experiences(user_experience_id: int, db: Session = Depends(get_db)):
    _user_experiences = crud.get_user_experience_by_id(db, user_experience_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_experiences)


@router_user_experience.get("/getExperiencesByUserId/{user_id}")
async def get_user_experiences(user_id: int, db: Session = Depends(get_db)):
    _user_experiences = crud.get_experience_by_user_id(db, user_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user_experiences)


@router_user_experience.patch("/{user_experience_id}")
async def update_user_experience(user_experience_id: int, request: RequestUserExperience, db: Session = Depends(get_db)):
    _user_experience = crud.update_user_experience(db, user_experience_id=user_experience_id,
                                                   user_experience=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_user_experience)


@router_user_experience.delete("/{user_experience_id}")
async def delete_user_experience(user_experience_id: int,  db: Session = Depends(get_db)):
    crud.remove_user_experience(db, user_experience_id=user_experience_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
