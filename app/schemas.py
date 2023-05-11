from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class Config:
    orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class CitySchema(BaseModel):
    id: Optional[int] = None
    name: str
    uf: str


class RequestCity(BaseModel):
    parameter: CitySchema = Field(...)


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    password: str
    email: str
    phone: str
    address: str
    # city_id: int
    # hardskill_id: int
    # softskill_id: int
    # formation_id: int
    # experience_id: int


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)
