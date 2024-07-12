
from dataclasses import dataclass

from pymongo.database import Database

from api.constants import Collection
from api.services.mixins.crud import CRUDMixin
from api.contract.library import LibraryInput, Library


@dataclass(frozen=True)
class LibraryService(CRUDMixin[LibraryInput, Library]):
    """Service for interacting with Libraries."""

    _collection = Collection.Library
    _OutputDocumentType = Library