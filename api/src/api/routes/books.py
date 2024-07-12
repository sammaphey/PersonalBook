from fastapi import APIRouter, Body, Query, status

from api.contract.search import Search, SearchInput
from api.services.factory import ServiceFactory
from api.contract.book import BookInput, Book, BookUpdate
from api.functions import partial


router = APIRouter()

BOOK_SERVICE = ServiceFactory().create_book_service()


@router.post(
    "/search",
    tags=["books"],
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
    return BOOK_SERVICE.search(params=params)


@router.post(
    "",
    tags=["books"],
    response_description="A list of ids representing the books created.",
    status_code=status.HTTP_201_CREATED,
    response_model=list[str],
    response_model_exclude_none=True,
)
async def create(
    books: list[BookInput] = Body(
        ...,
        description="A list of books to create.",
    ),
):
    """Create the given books in the database."""
    return BOOK_SERVICE.create(data=books)


@router.get(
    "",
    tags=["books"],
    response_description="A list of book responses.",
    status_code=status.HTTP_200_OK,
    response_model=list[Book],
    response_model_exclude_none=True,
)
async def read(
    ids: list[str] = Query(
        ...,
        description="The ids of the books to read.",
    ),
):
    """Read all of the given books from the database."""
    return BOOK_SERVICE.read(ids=ids)


@router.put(
    "",
    tags=["books"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update(
    data: dict[str, BookUpdate] = Body(
        ...,
        description="A mapping of book id to the updated information.",
    ),
):
    """Update all of the given books in the database."""
    return BOOK_SERVICE.update(data=data)


@router.delete(
    "",
    tags=["books"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    ids: list[str] = Query(
        ...,
        description="The ids of the books to delete.",
    ),
):
    """Delete all of the given books in the database."""
    return BOOK_SERVICE.delete(ids=ids)