from datetime import datetime
from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    """Representation of a documents metadata."""

    created_date: datetime = Field(default_factory=lambda: datetime.now())
    """The date the document was created."""

    updated_date: datetime = Field(default_factory=lambda: datetime.now())
    """The date the document was last updated."""