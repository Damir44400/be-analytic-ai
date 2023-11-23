import datetime

from app.database import Base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)


class Genre(Base):
    __tablename__ = "Genre"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)

    anime = relationship("GenreAnime", back_populates="genre")


class GenreAnime(Base):
    __tablename__ = "GenreAnime"

    id = Column(Integer, index=True, primary_key=True)
    genre_id = Column(Integer, ForeignKey("Genre.id"))
    anime_id = Column(Integer, ForeignKey("Anime.id"))

    anime = relationship("Anime", back_populates="genre")
    genre = relationship("Genre", back_populates="anime")


class Anime(Base):
    __tablename__ = "Anime"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, nullable=False, index=True, unique=True)
    cover = Column(String, nullable=False)
    date_announce = Column(DateTime, nullable=True)
    country = Column(String, default="Japan")
    description = Column(String, nullable=False)
    date_uploaded = Column(DateTime, default=datetime.datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.datetime.utcnow)
    studio_id = Column(Integer, ForeignKey("Studio.id"), nullable=True)
    producer_id = Column(Integer, ForeignKey("Producer.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("Category.id"))
    genre = relationship("GenreAnime", back_populates="anime")


class Role(Base):
    __tablename__ = "Role"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    permissions = Column(JSON, default={})


class AnimeChapter(Base):
    __tablename__ = "AnimeChapter"

    id = Column(Integer, index=True, primary_key=True)
    anime_video = Column(String, nullable=False)
    anime_id = Column(Integer, ForeignKey("Anime.id"))


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    profile_photo = Column(String)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(DateTime, default=datetime.datetime.now)
    role_id = Column(Integer, ForeignKey("Role.id"), default=2)

    roles = relationship("Role")


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    stars = Column(Integer)

    anime_id = Column(Integer, ForeignKey("Anime.id"))


class Producer(Base):
    __tablename__ = "Producer"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)


class Studio(Base):
    __tablename__ = "Studio"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
