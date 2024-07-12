"""CLI entrypoint for starting the API with logging."""

import os
from enum import StrEnum, auto
from pathlib import Path
from typing import Optional

import typer
import uvicorn
from loguru import logger as LOGGER
from rich import print

from api.constants import DEFAULT_BASE_PATH, PROJECT_ROOT
from api.settings import get_settings

settings = get_settings()
app = typer.Typer()


class LogLevel(StrEnum):
    """Definition of allowed log levels."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        """
        Make `auto` return enum values in UPPER_CASE.

        See [this link
        ](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_) for more
        details.
        """
        return name.upper()

    CRITICAL = auto()
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    DEBUG = auto()


DEFAULT_LOG_PATH = DEFAULT_BASE_PATH / ".book/personalBook.log"


def setup_logging_env_vars(
    loglevel: str,
    logpath: Path | None = None,
    stderr: bool = False,
):
    """
    Set up the logging environment variables based on provided log params.

    :param loglevel: The level to use for logging.
    :param logpath: The path to put the logs under. If not specified, defaults to
      ``DEFAULT_LOG_PATH``.
    :param stderr: Whether or not logs should be displayed to stderr. Defaults to False.
    :returns: The loglevel used to setup logging.
    """
    logpath = logpath or DEFAULT_LOG_PATH
    logpath = os.environ.setdefault("BOOK_LOG_PATH", logpath.resolve().as_posix())

    loglevel = os.environ.setdefault("BOOK_LOG_LEVEL", loglevel)

    if stderr:
        os.environ["BOOK_LOG_STDERR"] = str(stderr)

    return loglevel


@app.callback(invoke_without_command=True)
def main(
    dev: bool = typer.Option(
        False,
        "--dev",
        "-d",
        help=(
            "Enable dev mode (authentication will always succeed). "
            "This can also be set via the BOOK_DEV_MODE environment variable."
        ),
    ),
    loglevel: LogLevel = typer.Option(
        "WARNING",
        "--loglevel",
        "-l",
        help=(
            "What level to log at. "
            "This can also be set via the BOOK_LOG_LEVEL environment variable."
        ),
    ),
    logpath: Optional[Path] = typer.Option(  # noqa UP007
        None,
        "--logpath",
        "-p",
        help=(
            "Where to put the log file. "
            "This can also be set via the BOOK_LOG_PATH environment variable."
        ),
    ),
    reload: bool = typer.Option(
        False, "--reload", "-r", help="Automatically reload on code changes."
    ),
    stderr: bool = typer.Option(
        False,
        "--stder",
        "-s",
        help=(
            "Display logs to stderr. "
            "This can also be set via the BOOK_LOG_STDERR environment variable"
        ),
    ),
    workers: Optional[int] = typer.Option(  # noqa UP007
        None, "--workers", "-w", help="Number of workers to use when running the app."
    ),
):
    """
    Application entry point for API.

    Set up the application based on the CLI/environment variables set.
    """
    log_level = setup_logging_env_vars(loglevel=loglevel, logpath=logpath, stderr=stderr).lower()
    LOGGER.debug("Logging environment variables successfully setup.")

    if reload and workers:
        print("Application cannot be run in a reload state with multiple workers.")  # noqa: T201
        raise typer.Exit(1)

    additional_args = {}
    if reload:
        additional_args["reload"] = reload
        additional_args["reload_dirs"] = [PROJECT_ROOT]

    if workers:
        additional_args["workers"] = workers

    if dev:
        LOGGER.warning("Running in dev mode, all authentication attempts will succeed.")

    os.environ["BOOK_DEV_MODE"] = str(dev)

    uvicorn.run(
        app="api.routes:app",
        host="0.0.0.0",
        port=settings.port,
        log_level=log_level,
        **additional_args,
    )


if __name__ == "__main__":
    app()
