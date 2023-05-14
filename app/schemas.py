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
    city_id: int
    hardskill_id: int
    softskill_id: int
    formation_id: int
    experience_id: int


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class SoftskillSchema(BaseModel):
    id: Optional[int] = None
    name: str


class RequestSoftskill(BaseModel):
    parameter: SoftskillSchema = Field(...)


class HardskillSchema(BaseModel):
    id: Optional[int] = None
    name: str


class RequestHardskill(BaseModel):
    parameter: HardskillSchema = Field(...)


class FormationSchema(BaseModel):
    id: Optional[int] = None
    curso: str
    instituicao: str
    periodo: str


class RequestFormation(BaseModel):
    parameter: FormationSchema = Field(...)


class ExperienceSchema(BaseModel):
    id: Optional[int] = None
    cargo: str
    empresa: str
    periodo: str


class RequestExperience(BaseModel):
    parameter: ExperienceSchema = Field(...)


class UserSoftskillSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    softskill_id: int


class RequestUserSoftskill(BaseModel):
    parameter: UserSoftskillSchema = Field(...)


class UserHardskillSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    hardskill_id: int


class RequestUserHardskill(BaseModel):
    parameter: UserHardskillSchema = Field(...)


class CompanySchema(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    cnpj: str
    password: str
    email: str
    phone_number: str
    address: str
    city_id: int
    joboffer_id: int


class RequestCompany(BaseModel):
    parameter: CompanySchema = Field(...)


class JobofferSchema(BaseModel):
    id: Optional[int] = None
    code: int
    name: str
    description: str
    company: str
    city_id: int


class RequestJoboffer(BaseModel):
    parameter: JobofferSchema = Field(...)


class ApplicationSchema(BaseModel):
    id: Optional[int] = None
    status_id: int
    joboffer_id: int
    user_id: int


class RequestApplication(BaseModel):
    parameter: ApplicationSchema = Field(...)


class StatusSchema(BaseModel):
    id: Optional[int] = None
    status: str


class RequestStatus(BaseModel):
    parameter: StatusSchema = Field(...)
