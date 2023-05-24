from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field, validator
from pydantic.generics import GenericModel
from security import get_password_hash

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
    hash_password: str = Field(alias='password')
    email: str
    phone: str
    address_number: str
    address_neighborhood: str
    address: str
    address_complement: str
    city_id: int
    formation_id: int
    experience_id: int

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        return get_password_hash(v)


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class UserUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    hash_password: Optional[str] = Field(alias='password')
    email: Optional[str]
    phone: Optional[str]
    address_number: Optional[str]
    address_neighborhood: Optional[str]
    address: Optional[str]
    address_complement: Optional[str]
    city_id: Optional[int]
    formation_id: Optional[int]
    experience_id: Optional[int]

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        if v:
            return get_password_hash(v)
        return v


class RequestUserUpdate(BaseModel):
    parameter: UserUpdate = Field(...)


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
    course: str
    date: str
    institution_id: int


class RequestFormation(BaseModel):
    parameter: FormationSchema = Field(...)


class ExperienceSchema(BaseModel):
    id: Optional[int] = None
    company: str
    date: str
    position_id: int


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
    address_number: str
    address_neighborhood: str
    address: str
    address_complement: str
    city_id: int


class RequestCompany(BaseModel):
    parameter: CompanySchema = Field(...)


class JobofferSchema(BaseModel):
    id: Optional[int] = None
    code: int
    name: str
    description: str
    city_id: int
    company_id: int
    position_id: int


class RequestJoboffer(BaseModel):
    parameter: JobofferSchema = Field(...)


class ApplicationSchema(BaseModel):
    id: Optional[int] = None
    date: str
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


class PositionSchema(BaseModel):
    id: Optional[int] = None
    name: str


class RequestPosition(BaseModel):
    parameter: PositionSchema = Field(...)


class InstitutionSchema(BaseModel):
    id: Optional[int] = None
    name: str


class RequestInstitution(BaseModel):
    parameter: InstitutionSchema = Field(...)
