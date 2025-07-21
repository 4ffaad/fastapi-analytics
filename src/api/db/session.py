import sqlmodel 
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL, DB_TIMEZONE
import timescaledb

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set. Please configure it in your environment variables.")

engine = timescaledb.create_engine(DATABASE_URL, timezone=DB_TIMEZONE)

def init_db():
    print("Initializing database connection...")
    SQLModel.metadata.create_all(engine)
    print("Creating hypertables")
    timescaledb.metadata.create_all(engine)

def get_session():
    """
    Create a new SQLModel session.
    """
    with Session(engine) as session:
        yield session
        