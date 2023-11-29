import datetime
from sqlalchemy import Column, String, Date, Integer, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    animes = relationship("Anime", back_populates="category", cascade="all,delete")


class Genre(Base):
    __tablename__ = "Genre"
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    animes = relationship("GenreAnime", back_populates="genre", cascade="all,delete")


class GenreAnime(Base):
    __tablename__ = "GenreAnime"
    id = Column(Integer, index=True, primary_key=True)
    genre_id = Column(Integer, ForeignKey("Genre.id"))
    anime_id = Column(Integer, ForeignKey("Anime.id"))

    anime = relationship("Anime", back_populates="genres", cascade="all,delete")
    genre = relationship("Genre", back_populates="animes", cascade="all,delete")


class Anime(Base):
    __tablename__ = "Anime"
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, nullable=False, index=True, unique=True)
    cover = Column(String, nullable=False)
    country = Column(String, default="Japan")
    description = Column(String, nullable=False)
    date_uploaded = Column(DateTime, default=datetime.datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.datetime.utcnow)
    studio_id = Column(Integer, ForeignKey("Studio.id"), nullable=True)
    producer_id = Column(Integer, ForeignKey("Producer.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("Category.id"))
    date_announce = Column(Integer, ForeignKey("AnimeDateCreated.year"))

    genres = relationship("GenreAnime", back_populates="anime", cascade="all,delete")
    category = relationship("Category", back_populates="animes", cascade="all,delete")
    chapters = relationship("AnimeChapter", back_populates="anime", cascade="all,delete")
    date_announces = relationship("AnimeDateCreated", back_populates="animes")
    producer = relationship("Producer", back_populates="animes")
    studio = relationship("Studio", back_populates="animes")


class AnimeDateCreated(Base):
    __tablename__ = "AnimeDateCreated"
    id = Column(Integer, index=True, primary_key=True)
    year = Column(Integer, index=True, unique=True)
    animes = relationship("Anime", back_populates="date_announces", cascade="all,delete")


class Role(Base):
    __tablename__ = "Role"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    permissions = Column(JSON, default={})
    users = relationship("User", back_populates="role", cascade="all,delete")


class AnimeChapter(Base):
    __tablename__ = "AnimeChapter"
    id = Column(Integer, index=True, primary_key=True)
    anime_video = Column(String, nullable=False)
    chapter = Column(Integer)
    anime_id = Column(Integer, ForeignKey("Anime.id", ondelete="CASCADE"))
    anime = relationship("Anime", back_populates="chapters", cascade="all,delete")


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    profile_photo = Column(String, nullable=True)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)
    role_id = Column(Integer, ForeignKey("Role.id"), default=2)
    role = relationship("Role", back_populates="users", cascade="all,delete")


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    stars = Column(Integer)
    user_id = Column(Integer, ForeignKey('User.id', ondelete="CASCADE"))
    anime_id = Column(Integer, ForeignKey("Anime.id", ondelete="CASCADE"))


class Producer(Base):
    __tablename__ = "Producer"
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    animes = relationship("Anime", back_populates="producer", cascade="all,delete")


class Studio(Base):
    __tablename__ = "Studio"
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    animes = relationship("Anime", back_populates="studio", cascade="all,delete")
