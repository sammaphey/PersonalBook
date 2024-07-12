from dataclasses import dataclass
from typing import Generic

from pymongo.database import Database

from api.services.mixins import InputDocument, OutputDocument
from api.services.mixins.create import CreateMixin
from api.services.mixins.delete import DeleteMixin
from api.services.mixins.read import ReadMixin
from api.services.mixins.update import UpdateMixin
from api.constants import Collection



@dataclass(frozen=True)
class CRUDMixin(
    Generic[InputDocument, OutputDocument],
    CreateMixin[InputDocument],
    ReadMixin[OutputDocument],
    UpdateMixin[InputDocument],
    DeleteMixin,
):
    """Mixin representing all crud methods."""