from typing import Optional
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: Optional[int]
    name: str
    email: str
    phone: str
    address_number: str
    address_neighborhood: str
    address: str
    address_complement: str
    city_id: int
    formation_id: int
    experience_id: int
