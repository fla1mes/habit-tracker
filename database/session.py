from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DataBaseURL = "sqlite:///habit_tracker.db"
engine = create_engine(DataBaseURL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit = False)

Base = declarative_base()