from sqlalchemy import Column, Integer, String, ForeignKey
from config import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    uf = Column(String(2))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    password = Column(String(255))
    email = Column(String(100))
    phone = Column(String(11))
    address = Column(String(255))
    # city_id = Column(Integer, ForeignKey("city.id"))
    # hardskill_id = Column(Integer, ForeignKey("hardskill.id"))
    # softskill_id = Column(Integer, ForeignKey("softskill.id"))
    # formation_id = Column(Integer, ForeignKey("formation.id"))
    # experience_id = Column(Integer, ForeignKey("experience.id"))
