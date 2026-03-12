# /// script
# requires-python = ">=3.12"
# dependencies = ["sqlalchemy"]
# ///
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    sqft = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    description = Column(Text, default="")
    image_url = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


DATABASE_URL = "sqlite:///./realtor.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
