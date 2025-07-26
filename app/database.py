from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.schema import Base

DATABASE_URL = "postgresql://username:password@host:port/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)
