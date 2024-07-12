
from dataclasses import dataclass
from typing import Generic
from pymongo.database import Database

from api.services.mixins import InputDocument
from api.contract.document import DocumentMetadata
from api.constants import Collection


@dataclass(frozen=True)
class CreateMixin(Generic[InputDocument]):
    _DB: Database
    _collection: Collection

    def create(self, *, data: list[InputDocument]) -> list[str]:
        """
        Create data in a collection.

        :param data: A list of documents to create.
        :return: A list of ids that represent the documents created.
        """
        return [str(s) for s in self._DB[self._collection].insert_many([
            {
                **d.model_dump(exclude_none=True),
                "metadata": DocumentMetadata().model_dump(exclude_none=True)
            } for d in data
        ]).inserted_ids]