from models.base import Base

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Float

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    gpa: Mapped[float] = mapped_column(Float)
# forward declaration to prevent circular imports
    addresses: Mapped[List["Address"]] = relationship(back_populates="student",
                                                    lazy="selectin", 
                                                    cascade="all, delete-orphan")
    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, name{self.name} gpa{self.gpa})"