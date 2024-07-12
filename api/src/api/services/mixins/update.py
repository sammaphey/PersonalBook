
from dataclasses import dataclass
from typing import Generic
from bson import ObjectId
from pymongo import UpdateOne
from pymongo.database import Database

from api.services.mixins import InputDocument
from api.constants import Collection
from api.contract.document import DocumentMetadata


@dataclass(frozen=True)
class UpdateMixin(Generic[InputDocument]):
    _DB: Database
    _collection: Collection

    def update(self, *, data: dict[str, InputDocument]):
        """
        Update documents in a collection.

        :param data: A mapping of the document id and the new document.
        """
        # Get the document to read it's created_date
        response = self._DB[self._collection].find({"_id": {"$in": [ObjectId(s) for s in data]}})
        response = {str(r["_id"]): r for r in response}

        self._DB[self._collection].bulk_write([
            UpdateOne({"_id": ObjectId(id)}, {
                "$set": {
                    **update.model_dump(exclude_none=True),
                    "metadata": DocumentMetadata(
                        created_date=response[id]["metadata"]["created_date"]
                    ).model_dump(exclude_none=True)
                }
            }) for id, update in data.items()
        ])