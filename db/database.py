from sqlalchemy import create_engine
from models import Base

def create_database(db_url: str = "sqlite:///students.db", echo_val: bool = True):
    engine = create_engine(db_url, echo=echo_val)
    Base.metadata.create_all(engine)

def drop_database(db_url: str = "sqlite:///students.db", echo_val: bool = True):
    engine = create_engine(db_url, echo=echo_val)
    Base.metadata.drop_all(engine)