from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

engine = create_engine("sqlite:///db.sqlite", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)