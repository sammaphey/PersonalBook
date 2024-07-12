
from dataclasses import dataclass

from api.constants import Collection
from api.services.mixins.crud import CRUDMixin
from api.contract.user import UserInput, User


@dataclass(frozen=True)
class UserService(CRUDMixin[UserInput, User]):
    """Service for interacting with Users."""

    _collection = Collection.User
    _OutputDocumentType = User