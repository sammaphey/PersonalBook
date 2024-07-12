from enum import StrEnum, auto
from pydantic import BaseModel

from api.contract.document import DocumentMetadata
from api.functions import partial

class Genre(StrEnum):
    """Genres for books."""

    fantasy = auto()
    horror = auto()
    sci_fi = auto()
    romance = auto()
    mystery = auto()

class UserInput(BaseModel):
    """Representation of a user in the application."""

    name: str
    """The name of the user."""

    favorite_genres: list[Genre] = []
    """The favorite genres for this user."""


class User(UserInput):
    """Representation of a user in the application."""

    metadata: DocumentMetadata
    """Metadata representing the user."""


@partial
class UserUpdate(UserInput):
    """Representation of a user for updates."""