from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, List

class StudentCreate(BaseModel):
    name: str
    fullname: Optional[str]
    gpa: float

    addresses: List[EmailStr] = []
    model_config = ConfigDict(str_max_length=50)

class StudentUpdate(BaseModel):
    name: Optional[str]
    fullname: Optional[str]
    gpa: Optional[float] 

    addresses: Optional[List[EmailStr]]
    model_config = ConfigDict(str_max_length=50)

class AddressRead(BaseModel):
    id: int
    address: EmailStr
    student_id: int 

    model_config = ConfigDict(from_attributes=True)

class StudentRead(BaseModel):
    id: int
    name: str
    fullname: Optional[str]
    gpa: float

    addresses: List[AddressRead]
    model_config = ConfigDict(from_attributes=True)