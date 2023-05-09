from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, RequestCity

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_city_service(request: RequestCity, db: Session = Depends(get_db)):
    crud.create_city(db, city=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="City created successfully").dict(exclude_none=True)


@router.get("/")
async def get_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _cities = crud.get_city(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_cities)


@router.patch("/update")
async def update_city(request: RequestCity, db: Session = Depends(get_db)):
    _city = crud.update_city(db, city_id=request.parameter.id,
                             name=request.parameter.name, uf=request.parameter.uf)
    return Response(status="Ok", code="200", message="Success update data", result=_city)


@router.delete("/delete")
async def delete_city(request: RequestCity,  db: Session = Depends(get_db)):
    crud.remove_city(db, city_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
