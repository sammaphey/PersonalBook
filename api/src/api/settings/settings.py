"""Module for loading application config."""

from __future__ import annotations

from functools import cache
from typing import Annotated

from loguru import logger as LOGGER
from pydantic import (
    Field,
    HttpUrl,
    SecretStr,
    ValidationError,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    App settings.

    This class is typically not instantiated directly. Use `api.settings.get_settings` instead.
    """

    model_config = SettingsConfigDict(env_prefix="book_", env_file=(".example.env", ".env"))

    port: Annotated[int, Field(5000, gt=0, lt=2**16)]  # port numbers may be from 1-65535
    api_secret: SecretStr
    origins: list[HttpUrl]

    mongo: str = "mongodb://localhost"
    mongo_db_name: str
    mongo_username: str
    mongo_password: SecretStr


@cache
def get_settings():
    """
    Get the Darc app settings.

    Settings will be read from `.example.env` file found in the working directory, then from a
    `.env` file, then finally from default values in the Settings class. Manually set environment
    variables will override everything.

    Environment variables should use the prefix `DARC_` and are not case-sensitive.

    To use:

        ```python
        from api.settings import get_settings

        settings = get_settings()

        print(settings.email)
        ```
    """
    try:
        settings = Settings()
    except ValidationError as e:
        LOGGER.critical(
            "Unable to instantiate Settings, make sure all required environment variables are "
            f"set or .env file is present in current working directory; {e}"
        )
        raise SystemExit(1)
    LOGGER.debug(f"Using {settings=}")
    return settings
