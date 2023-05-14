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
    address_number = Column(String(5))
    address_neighborhood = Column(String(255))
    address_complement = Column(String(255))
    city_id = Column(Integer, ForeignKey("city.id"))
    formation_id = Column(Integer, ForeignKey("formation.id"))
    experience_id = Column(Integer, ForeignKey("experience.id"))


class Softskill(Base):
    __tablename__ = "softskill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))


class Hardskill(Base):
    __tablename__ = "hardskill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))


class Formation(Base):
    __tablename__ = "formation"

    id = Column(Integer, primary_key=True, index=True)
    course = Column(String(255))
    institution = Column(String(255))
    date = Column(String(255))


class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255))
    date = Column(String(255))
    position_id = Column(Integer, ForeignKey("position.id"))


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    cnpj = Column(String(18))
    password = Column(String(255))
    email = Column(String(100))
    phone_number = Column(String(11))
    address = Column(String(255))
    address_number = Column(String(5))
    address_neighborhood = Column(String(255))
    address_complement = Column(String(255))
    city_id = Column(Integer, ForeignKey("city.id"))


class Joboffer(Base):
    __tablename__ = "joboffer"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    name = Column(String(100))
    description = Column(String(255))
    city_id = Column(Integer, ForeignKey("city.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    position_id = Column(Integer, ForeignKey("position.id"))


class Application(Base):
    __tablename__ = "application"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(100))
    status_id = Column(Integer, ForeignKey("status.id"))
    joboffer_id = Column(Integer, ForeignKey("joboffer.id"))
    user_id = Column(Integer, ForeignKey("user.id"))


class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(255))


class UserSoftskill(Base):
    __tablename__ = "user_softskill"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    softskill_id = Column(Integer, ForeignKey("softskill.id"))


class UserHardskill(Base):
    __tablename__ = "user_hardskill"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    hardskill_id = Column(Integer, ForeignKey("hardskill.id"))


class Position(Base):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
