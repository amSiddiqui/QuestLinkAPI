"""
This module is used to set up the SQLAlchemy database engine, session, and base class.
The database URL is retrieved from the application settings.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)
Session = sessionmaker(bind=engine, expire_on_commit=False, autocommit=False, autoflush=False)
Base = declarative_base()

