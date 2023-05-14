from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestExperience

import crud

router_experience = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# experience


@router_experience.post("/")
async def create_experience_service(request: RequestExperience, db: Session = Depends(get_db)):
    crud.create_experience(db, experience=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Experience created successfully").dict(exclude_none=True)


@router_experience.get("/")
async def get_experiences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _experiences = crud.get_experience(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_experiences)


@router_experience.get("/{experience_id}")
async def get_experiences(experience_id: int, db: Session = Depends(get_db)):
    _experiences = crud.get_experience_by_id(db, experience_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_experiences)


@router_experience.patch("/{experience_id}")
async def update_experience(experience_id: int, request: RequestExperience, db: Session = Depends(get_db)):
    _experience = crud.update_experience(db, experience_id=experience_id,
                                         experience=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_experience)


@router_experience.delete("/{experience_id}")
async def delete_experience(experience_id: int,  db: Session = Depends(get_db)):
    crud.remove_experience(db, experience_id=experience_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
