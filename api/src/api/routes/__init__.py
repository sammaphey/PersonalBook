from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import libraries, users
from api.settings import get_settings

settings = get_settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Have to strip off the trailing `/` that get's auto added by Pydantic
    # See bug: https://github.com/pydantic/pydantic/issues/7186
    allow_origins=[str(url).removesuffix("/") for url in settings.origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(libraries.router, prefix="/libraries", tags=["libraries"])
