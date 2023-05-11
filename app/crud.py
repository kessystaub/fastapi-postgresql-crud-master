from sqlalchemy.orm import Session
from models import City, User
from schemas import CitySchema

import schemas
import models
# city


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


def update_city(db: Session, city_id: int, name: str, uf: str):
    _city = get_city_by_id(db=db, city_id=city_id)

    _city.name = name
    _city.uf = uf

    db.commit()
    db.refresh(_city)
    return _city


def remove_city(db: Session, city_id: int):
    _city = get_city_by_id(db=db, city_id=city_id)
    db.delete(_city)
    db.commit()

# user


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserSchema):
    _user = get_user_by_id(db=db, user_id=user_id)

    _user.name = user.name
    _user.password: user.password
    _user.email: user.email
    _user.phone: user.phone
    _user.address: user.address
    # _user.city_id: user.city_id
    # _user.hardskill_id: user.hardskill_id
    # _user.softskill_id: user.softskill_id
    # _user.formation_id: user.formation_id
    # _user.experience_id: user.experience_id

    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()
