from models import Base

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Float, ForeignKey

class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(40))
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))

# forward declaration to prevent circular imports
    student: Mapped["Student"] = relationship(back_populates="addresses")

    # this function decides how this object prints 
    # when print() is called on it
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.address!r})"