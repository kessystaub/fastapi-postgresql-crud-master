from sqlalchemy import Column, Integer, String
from config import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    uf = Column(String)
