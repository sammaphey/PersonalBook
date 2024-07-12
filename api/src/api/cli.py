"""Setup CLI."""

from importlib import metadata

import typer

import api.launcher as launcher

app = typer.Typer()
app.add_typer(
    launcher.app,
    name="launch",
    help="Launch the application",
)


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(
        False, "--version", "-v", help="Display version information and exit."
    ),
):
    """Top-level entrypoint for the darcpy application."""
    if version:
        print(f"api version {metadata.version('api')}")  # noqa: T201
        raise typer.Exit()


if __name__ == "__main__":
    app()
