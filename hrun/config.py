"""Configuration command"""
from typing_extensions import Annotated
from pathlib import Path
import os
import subprocess
import typer

app = typer.Typer(no_args_is_help=True)


@app.callback()
def config(
    init: Annotated[bool, typer.Option("--init", "-i")] = False,
    edit: Annotated[bool, typer.Option("--edit", "-e")] = False
):
    """
    Persistent configuration for history-runner.

    Explicitly call --init to create the config.toml file
    in the default path of your system.
    """
    data_dir = Path(typer.get_app_dir("history-runner"))
    config_file = data_dir / "config.toml"
    if init:
        if config_file.exists():
            print(f"Config file already at: {config_file}")
        else:
            print(f"Creating config file at: {config_file}")
            config_file.touch()
    elif edit is not False:
        editor = os.getenv("EDITOR")
        subprocess.run([editor, config_file])
