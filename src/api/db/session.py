import sqlmodel 
from sqlmodel import SQLModel
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set. Please configure it in your environment variables.")

engine = sqlmodel.create_engine("sqlite:///./test.db", echo=True)

def init_db():
    print("Initializing database connection...")
    SQLModel.metadata.create_all(engine)
