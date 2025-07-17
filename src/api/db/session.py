import sqlmodel 
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set. Please configure it in your environment variables.")

engine = sqlmodel.create_engine(DATABASE_URL, echo=True)

def init_db():
    print("Initializing database connection...")
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Create a new SQLModel session.
    """
    with Session(engine) as session:
        yield session
        