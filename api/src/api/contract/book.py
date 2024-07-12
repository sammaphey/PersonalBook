from pydantic import BaseModel

from api.contract.document import DocumentMetadata
from api.functions import partial

class BookInput(BaseModel):
    """Representation of a book in the application."""

    isbn: str
    """The ISBN number of the book."""

    title: str
    """The title of the book."""

    author: list[str]
    """The author of the book."""

    synopsis: str
    """The synopsis of the book."""

    genre: list[str] = []
    """The genres of the book."""


class Book(BookInput):
    """Representation of a book in the application."""

    metadata: DocumentMetadata
    """Metadata representing the book."""


@partial
class BookUpdate(BookInput):
    """Representation of a book for updates."""