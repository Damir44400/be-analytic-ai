import datetime

from app.database import Base
from sqlalchemy import Column, String, DateTime, Integer


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, index=True, primary_key=True)
    profile_photo = Column(String)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(DateTime, default=datetime.datetime.now)
