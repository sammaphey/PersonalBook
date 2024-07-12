from __future__ import annotations

from functools import cache
from typing import ClassVar, NamedTuple

from pydantic import SecretStr
from pymongo.database import Database
from pymongo import MongoClient

from api.services.library import LibraryService
from api.services.user import UserService

from api.settings import get_settings
from api.constants import Collection
from api.contract.library import Library
from api.contract.user import User

settings = get_settings()

class StoreKey(NamedTuple):
    """Tuple alias for the input parameters to instantiate a DAOFactory."""

    mongo: str
    mongo_username: str
    mongo_password: SecretStr
    mongo_db_name: str


class ServiceFactory:
    """Build services."""

    _DB: Database = None
    _STORE: ClassVar[dict[StoreKey, ServiceFactory]] = {}

    def __new__(cls):
        """Initialize a service factory."""
        key = StoreKey(
            mongo=settings.mongo,
            mongo_username=settings.mongo_username,
            mongo_password=settings.mongo_password,
            mongo_db_name=settings.mongo_db_name,
        )
        if key in cls._STORE:
            # DAOFactory already initialized
            return cls._STORE[key]
        self = cls._STORE[key] = object.__new__(ServiceFactory)
        self._DB = MongoClient(
            settings.mongo,
            username=settings.mongo_username,
            password=settings.mongo_password.get_secret_value(),
        )[settings.mongo_db_name]

        return self

    @cache
    def create_library_service(self):
        """
        Create a service for interacting with library data.

        :returns: A ``LibraryService``.
        """
        return LibraryService(_DB=self._DB, _collection=Collection.Library, _OutputDocumentType=Library)

    @cache
    def create_user_service(self):
        """
        Create a service for interacting with user data.

        :returns: A ``UserService``.
        """
        return UserService(_DB=self._DB, _collection=Collection.User, _OutputDocumentType=User)