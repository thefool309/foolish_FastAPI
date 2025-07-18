
from fastapi import FastAPI, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
# from sqlalchemy import text
# from sqlalchemy.orm import Session as sesh
# from sqlalchemy.orm import sessionmaker as seshfac

from db import create_database, create_student, StudentCreate, StudentRead, list_students, get_student

engine = create_engine("sqlite:///students.db", echo=True)

app = FastAPI()

create_database()

# check if the api is up
@app.get("/")
def read_root():
    return{"API Working": "Ready!"}
# returns a student as json
@app.get("/students", response_model=list[StudentRead], summary="List all students in database")
def list_students_endpoint():
    try:
        return list_students()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"unexpected error: {str(e)}"
        )
#takes in a student_id to find a student 
# and return the student as json
@app.get("/students/{student_id}", response_model=StudentRead, summary="Get a specific student by ID")
def get_student_by_id_endpoint(student_id: int):
    try:
        return get_student(student_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"unexpected error: {str(e)}"
        )
# takes in json data with the request to insert a student into the database       
@app.post("/students", summary="Create a new student from json data")
def create_student_endpoint(student_data: StudentCreate):
    try:
        student = create_student(student_data)
        return student
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database constraint violated (e.g., duplicate or missing foreign key)"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"unexpected error: {str(e)}"
        )

