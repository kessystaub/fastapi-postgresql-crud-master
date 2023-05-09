from sqlalchemy.orm import Session
from models import City
from schemas import CitySchema


def get_city(db: Session, skip: int = 0, limit: int = 100):
    return db.query(City).offset(skip).limit(limit).all()


def get_city_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


def create_city(db: Session, city: CitySchema):
    _city = City(name=city.name, uf=city.uf)
    db.add(_city)
    db.commit()
    db.refresh(_city)
    return _city


def remove_city(db: Session, city_id: int):
    _city = get_city_by_id(db=db, city_id=city_id)
    print("cidade: ", _city)
    db.delete(_city)
    db.commit()


def update_city(db: Session, city_id: int, name: str, uf: str):
    _city = get_city_by_id(db=db, city_id=city_id)

    _city.name = name
    _city.uf = uf

    db.commit()
    db.refresh(_city)
    return _city
