from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("sqlite:///students.db", echo=True)

app = FastAPI()

with engine.connect() as conn:
    result = conn.execute(text("SELECT 'UWU owo >^w^<'"))
    print(result.all())
    conn.execute(text("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, age INTEGER NOT NULL, gpa FLOAT NOT NULL)"))
    conn.commit()



@app.get("/")
def read_root():
    return{"API Working": "Ready!"}