from enum import StrEnum, auto
import os
from pathlib import Path


DEFAULT_BASE_PATH = (
    Path(os.environ["XDG_STATE_HOME"]) if os.environ.get("XDG_STATE_HOME") else Path.home()
)
"""The default path to use when writing logs or files."""

PROJECT_ROOT = Path(__file__).parent
"""The path to the root of the api project."""

class Collection(StrEnum):
    """The collections to manipulate."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        """
        Make `auto` return enum values in the first char in upper case.

        See [this link
        ](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_) for more
        details.
        """
        return name.title()

    Book = auto()
    User = auto()
    Library = auto()