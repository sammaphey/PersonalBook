from typing import Any
from pydantic import BaseModel


class Search(BaseModel):
    """Representation of a search response."""

    results: list[Any]
    """The results that matched the search."""

    total: int
    """The total number of matching results."""

class SearchInput(BaseModel):
    """Representation of a search."""
