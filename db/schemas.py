from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

class StudentCreate(BaseModel):
    name: str
    fullname: Optional[str]
    gpa: float

    address:List[EmailStr] = []
    model_config = ConfigDict(str_max_length=50)

class StudentUpdate(BaseModel):
    name: Optional[str]
    fullname: Optional[str]
    gpa: Optional[float] 

    address: Optional[List[EmailStr]]
    model_config = ConfigDict(str_max_length=50)

class AddressRead(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class StudentRead(BaseModel):
