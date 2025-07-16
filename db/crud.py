from sqlalchemy import create_engine
from sqlalchemy.orm import Session, selectinload

from db.database import SessionLocal
from db.schemas import StudentCreate, StudentRead, StudentUpdate
from models import Student, Address


def create_student(student_data: StudentCreate) -> Student:

    with SessionLocal() as session, session.begin():
        # create the address objects
        address_objs = [Address(address=email) for email in student_data.addresses]
        # create the Student object
        student = Student(
            name=student_data.name,
            fullname=student_data.fullname,
            gpa=student_data.gpa,
            addresses=address_objs
        )

        # add to the session
        session.add(student)
        session.flush()
        session.refresh(student) # this makes sure the autoincremented ID generates

        return student

def list_students() -> list[StudentRead]:
    with SessionLocal() as session, session.begin():
        # eagerly load so we don't encounter errors 
        # when converting to pydantic objects
        students = session.query(Student).options(selectinload(Student.addresses)).all()
        for student in students:
            print(student.addresses)  # should be a list of Address objects
            print([type(a) for a in student.addresses])  # should show all <class 'models.Address'>

        return [StudentRead.model_validate(s) for s in students]

def get_student(student_id: int) -> StudentRead:
    with SessionLocal() as session, session.begin():
        student = session.query(Student).options(selectinload(Student.addresses)).get(student_id)

        # checking for an empty value in student
        if student is None:
            raise ValueError(f"Student with id {student_id} not found")
        
        return StudentRead.model_validate(student)
        
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 'UWU owo >^w^<'"))
#     print(result.all())
#     conn.execute(text("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER NOT NULL, gpa FLOAT NOT NULL)"))
#     conn.commit()

# stmt = text("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER NOT NULL, gpa FLOAT NOT NULL)")


# using the factory method vs the Session method 

# you can use the context manager interface 
# or frame out the try block

# this is one way to work with a session 
# but this would be considered the "longform"
# this is what's happening behind the scenes with the below
# with sesh(engine) as session:
#     try:
#         session.execute(stmt)
#     except:
#         session.rollback()
#         raise
#     else:
#         session.commit()

# short form of the above also making use of the sessionmaker
# factory method

# Session = seshfac(engine)

# with Session.begin() as session:
#     session.execute(stmt)
# # comits the transaction and closes the session