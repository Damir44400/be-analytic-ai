from app.database import Base
from sqlalchemy import Column, BigInteger, String


class User(Base):
    __tablename__ = "User"

    id = Column(BigInteger, index=True, primary_key=True)
    profile_photo = Column(String)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
