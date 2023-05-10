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


@router.post("/")
async def create_city_service(request: RequestCity, db: Session = Depends(get_db)):
    crud.create_city(db, city=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="City created successfully").dict(exclude_none=True)


@router.get("/")
async def get_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _cities = crud.get_city(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_cities)


@router.get("/{city_id}")
async def get_cities(city_id: int, db: Session = Depends(get_db)):
    _cities = crud.get_city_by_id(db, city_id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_cities)


@router.patch("/{city_id}")
async def update_city(city_id: int, request: RequestCity, db: Session = Depends(get_db)):
    _city = crud.update_city(db, city_id=city_id,
                             name=request.parameter.name, uf=request.parameter.uf)
    return Response(status="Ok", code="200", message="Success update data", result=_city)


@router.delete("/{city_id}")
async def delete_city(city_id: int,  db: Session = Depends(get_db)):
    crud.remove_city(db, city_id=city_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
