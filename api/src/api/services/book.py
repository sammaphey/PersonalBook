
from dataclasses import dataclass

from api.services.mixins.crud import CRUDMixin
from api.contract.book import Book, BookInput
from api.constants import Collection


@dataclass(frozen=True)
class BookService(CRUDMixin[BookInput, Book]):
    """Service for interacting with Books."""

    _collection = Collection.Book
    _OutputDocumentType = Book