from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestApplication

import crud

router_application = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# application


@router_application.post("/")
async def create_application_service(request: RequestApplication, db: Session = Depends(get_db)):
    crud.create_application(db, application=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Application created successfully").dict(exclude_none=True)


@router_application.get("/")
async def get_applications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _applications = crud.get_application(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_applications)


@router_application.get("/{application_id}")
async def get_applications(application_id: int, db: Session = Depends(get_db)):
    _applications = crud.get_application_by_id(db, application_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_applications)


@router_application.patch("/{application_id}")
async def update_application(application_id: int, request: RequestApplication, db: Session = Depends(get_db)):
    _application = crud.update_application(db, application_id=application_id,
                                           application=request.parameter)
    return Response(status="Ok", code="200", message="Success update data", result=_application)


@router_application.delete("/{application_id}")
async def delete_application(application_id: int,  db: Session = Depends(get_db)):
    crud.remove_application(db, application_id=application_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
