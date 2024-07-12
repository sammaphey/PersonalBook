from fastapi import APIRouter, Body, Query, status

from api.contract.search import Search, SearchInput
from api.services.factory import ServiceFactory
from api.contract.library import LibraryInput, Library, LibraryUpdate


router = APIRouter()

LIBRARY_SERVICE = ServiceFactory().create_library_service()


@router.post(
    "/search",
    tags=["libraries"],
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
    return LIBRARY_SERVICE.search(params=params)


@router.post(
    "/search",
    tags=["libraries"],
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
    """
    Execute a search given the params and return search results.

    Start values over 100 thousand items will see very degraded performance, always try to
    constrain your searches to have less than 50 thousand results.
    """
    return LIBRARY_SERVICE.search(params=params)


@router.post(
    "",
    tags=["libraries"],
    response_description="A list of ids representing the libraries created.",
    status_code=status.HTTP_201_CREATED,
    response_model=list[str],
    response_model_exclude_none=True,
)
async def create(
    libraries: list[LibraryInput] = Body(
        ...,
        description="A list of libraries to create.",
    ),
):
    """Create the given libraries in the database."""
    return LIBRARY_SERVICE.create(data=libraries)


@router.get(
    "",
    tags=["libraries"],
    response_description="A list of libraries responses.",
    status_code=status.HTTP_200_OK,
    response_model=list[Library],
    response_model_exclude_none=True,
)
async def read(
    ids: list[str] = Query(
        ...,
        description="The ids of the libraries to read.",
    ),
):
    """Read all of the given libraries from the database."""
    return LIBRARY_SERVICE.read(ids=ids)


@router.put(
    "",
    tags=["libraries"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    data: dict[str, LibraryUpdate] = Body(
        ...,
        description="A mapping of libraries id to the updated information.",
    ),
):
    """Update all of the given libraries in the database."""
    return LIBRARY_SERVICE.update(data=data)


@router.delete(
    "",
    tags=["libraries"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    ids: list[str] = Query(
        ...,
        description="The ids of the libraries to delete.",
    ),
):
    """Delete all of the given libraries in the database."""
    return LIBRARY_SERVICE.delete(ids=ids)