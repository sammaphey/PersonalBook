from pydantic import BaseModel

from api.contract.document import DocumentMetadata
from api.functions import partial

class BookEntries(BaseModel):
    """Representation of an entry in a library."""

    book_isbn: str
    """The isbn of the book."""

    read: bool = True
    """Whether or not the book has been read."""


class LibraryInput(BaseModel):
    """Representation of a book in the application."""

    user: str
    """The id of the user whose library this represents."""

    books: list[BookEntries] = []
    """The title of the book."""


class Library(LibraryInput):
    """Representation of a library in the application."""

    metadata: DocumentMetadata
    """Metadata representing the library."""


@partial
class LibraryUpdate(LibraryInput):
    """Representation of a library for updates."""
