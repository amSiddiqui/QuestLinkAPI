"""
This module is used to manage the configuration settings for the application.
It uses the pydantic BaseSettings class for settings management.
Environment variables are used for configuration, with defaults provided for each setting.
"""

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    This class is a subclass of pydantic's BaseSettings class.
    It defines the configuration settings for the application, 
    with environment variables as the source.
    If an environment variable is not set, it will use the provided default value.
    """
    PROJECT_TITLE: str = "Quest Link API"
    PROJECT_VERSION: str = "0.0.1"
    HOST_HTTP: str = os.environ.get("HOST_HTTP", "http://")
    HOST_URL: str = os.environ.get("HOST_URL", "localhost")
    HOST_PORT: int = int(os.environ.get("HOST_PORT", "8000"))
    BASE_URL: str = f"{HOST_HTTP}{HOST_URL}:{HOST_PORT}"
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///./app.db")
    DEBUG: bool = os.environ.get("DEBUG", False)


settings = Settings()