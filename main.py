from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session as sesh
from sqlalchemy.orm import sessionmaker as seshfac
engine = create_engine("sqlite:///students.db", echo=True)

app = FastAPI()

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 'UWU owo >^w^<'"))
#     print(result.all())
#     conn.execute(text("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER NOT NULL, gpa FLOAT NOT NULL)"))
#     conn.commit()

stmt = text("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER NOT NULL, gpa FLOAT NOT NULL)")


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

Session = seshfac(engine)

with Session.begin() as session:
    session.execute(stmt)
# comits the transaction and closes the session


# the beginning of our API 
@app.get("/")
def read_root():
    return{"API Working": "Ready!"}