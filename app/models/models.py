"""
This module defines the SQLAlchemy models for the application.
Each class represents a table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Table, Boolean
from app.db.session import Base


game_genre_association = Table(
    "game_genre_association",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("games.id")),
    Column("genre_id", Integer, ForeignKey("genres.id")),
)

game_platform_association = Table(
    "game_platform_association",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("games.id")),
    Column("platform_id", Integer, ForeignKey("platforms.id")),
)

game_age_rating_association = Table(
    "game_age_rating_association",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("games.id")),
    Column("age_rating_id", Integer, ForeignKey("age_ratings.id")),
)

game_company_association = Table(
    "game_company_association",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("games.id")),
    Column("company_id", Integer, ForeignKey("companies.id")),
    Column("developer", Boolean),
)

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    first_release_date = Column(DateTime)
    name = Column(String, index=True)
    summary = Column(String)
    url = Column(String)
    parent_game = Column(Integer, ForeignKey("games.id"))
    rating = Column(Float)
    rating_count = Column(Integer)
    storyline = Column(String)
    total_rating = Column(Float)
    total_rating_count = Column(Integer)


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(Integer)
    description = Column(String)
    name = Column(String, index=True)
    url = Column(String)
    parent = Column(Integer, ForeignKey("companies.id"))


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    category_description = Column(String)


class AgeRating(Base):
    __tablename__ = "age_ratings"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    rating = Column(Integer)
    rating_system = Column(String)
    rating_description = Column(String)


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    alternative_name = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    generation = Column(Integer)
    abbreviation = Column(String)
    summary = Column(String)
