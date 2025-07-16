from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
local_db_url: str = "sqlite:///students.db"
local_echo_val: bool = True
engine = create_engine(local_db_url, echo=local_echo_val)
SessionLocal = sessionmaker(bind=engine)

def create_database(db_url: str = "sqlite:///students.db", echo_val: bool = True):
    engine = create_engine(db_url, echo=echo_val)
    Base.metadata.create_all(engine)

def drop_database(db_url: str = "sqlite:///students.db", echo_val: bool = True):
    engine = create_engine(db_url, echo=echo_val)
    Base.metadata.drop_all(engine)