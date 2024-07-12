from fastapi import APIRouter, Body, Query, status

from api.contract.search import Search, SearchInput
from api.services.factory import ServiceFactory
from api.contract.user import User, UserInput, UserUpdate


router = APIRouter()


USER_SERVICE = ServiceFactory().create_user_service()


@router.post(
    "/search",
    tags=["users"],
    response_description="A search response object.",
    status_code=status.HTTP_200_OK,
    response_model=Search,
    response_model_exclude_none=True,
)
async def search(
    params: SearchInput = Body(
        ...,
        description="The search params to execute this search with.",
    ),
):
    """Execute a search given the params and return search results."""
    return USER_SERVICE.search(params=params)


@router.post(
    "",
    tags=["users"],
    response_description="A list of ids representing the users created.",
    status_code=status.HTTP_201_CREATED,
    response_model=list[str],
    response_model_exclude_none=True,
)
async def create(
    users: list[UserInput] = Body(
        ...,
        description="A list of users to create.",
    ),
):
    """Create the given users in the database."""
    return USER_SERVICE.create(data=users)


@router.get(
    "",
    tags=["users"],
    response_description="A list of user responses.",
    status_code=status.HTTP_200_OK,
    response_model=list[User],
    response_model_exclude_none=True,
)
async def read(
    ids: list[str] = Query(
        ...,
        description="The ids of the users to read.",
    ),
):
    """Read all of the given users from the database."""
    return USER_SERVICE.read(ids=ids)


@router.put(
    "",
    tags=["users"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    data: dict[str, UserUpdate] = Body(
        ...,
        description="A mapping of user id to the updated information.",
    ),
):
    """Update all of the given users in the database."""
    return USER_SERVICE.update(data=data)


@router.delete(
    "",
    tags=["users"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    ids: list[str] = Query(
        ...,
        description="The ids of the users to delete.",
    ),
):
    """Delete all of the given users in the database."""
    return USER_SERVICE.delete(ids=ids)