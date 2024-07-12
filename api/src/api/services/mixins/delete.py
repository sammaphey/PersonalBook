
from dataclasses import dataclass
from pymongo.database import Database

from api.constants import Collection


@dataclass(frozen=True)
class DeleteMixin:
    _DB: Database
    _collection: Collection

    def delete(self, *, ids: list[str]):
        """
        Delete data from a collection.

        :param ids: A list of ids to delete.
        """
        return self._DB[self._collection].delete_many({"_id": {"$in": ids}})