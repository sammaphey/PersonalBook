
from dataclasses import dataclass
from typing import Generic
from bson import ObjectId
from pymongo.database import Database

from api.services.mixins import OutputDocument
from api.constants import Collection


@dataclass(frozen=True)
class ReadMixin(Generic[OutputDocument]):
    _DB: Database
    _collection: Collection
    _OutputDocumentType: type[OutputDocument]

    def read(self, *, ids: list[str]) -> list[OutputDocument]:
        """
        Read documents from a collection.

        :param ids: A list of ids whose documents are to be read.
        :return: A list of documents representing the document that was read.
        """
        response = self._DB[self._collection].find({"_id": {"$in": [ObjectId(s) for s in ids]}})
        return [self._OutputDocumentType(**document) for document in response]