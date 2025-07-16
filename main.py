
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

# the beginning of our API 
@app.get("/")
def read_root():
    return{"API Working": "Ready!"}

@app.get("/students", response_model=list[StudentRead])
def list_students_endpoint():
    try:
        return list_students()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"unexpected error: {str(e)}"
        )

@app.get("/students/{student_id}", response_model=StudentRead)
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
        
@app.post("/students")
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

