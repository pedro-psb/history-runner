"""
Examples:
    hrun use 3.1.12 3.2.2 -- python app.py
    hrun use 3.1.12 3.2.2 -- time python app.py
    hrun use 3.1.12 3.2.2 -- python -m timeit app.py
    # discover case apps and run against versions
    hrun use 3.1.12 3.2.2 --case-dirs cases --entrypoint app.py
"""

import typer
from pathlib import Path
from typing_extensions import Annotated

app = typer.Typer(name="history-runner", no_args_is_help=True)


# Called before every command call

@app.callback()
def main():
    """
    history-runner is a tool for running a program (or program sets) across
    different versions (git tags or releases).
    """
    print("Running history-runner")

# Commands


@app.command()
def run(command: str, tags: list[str]):
    """
    Run a command across different git tags
    """
    print(f"Running '{command}' across {tags}")


@app.command()
def config(init: Annotated[bool, typer.Option("--init")] = False):
    """
    Persistent configuration for history-runner.

    Explicitly call --init to create the config.toml file
    in the default path of your system.
    """
    if init:
        data_dir = Path(typer.get_app_dir("history-runner"))
        config_file = data_dir / "config.toml"
        if config_file.exists():
            print(f"Config file already at: {config_file}")
        else:
            print(f"Creating config file at: {config_file}")
            config_file.touch()


if __name__ == "__main__":
    app()
