from typing import TypeVar

from pydantic import BaseModel


InputDocument = TypeVar("InputDocument", bound=BaseModel)
OutputDocument = TypeVar("OutputDocument", bound=BaseModel)