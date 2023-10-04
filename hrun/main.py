"""
Examples:
    hrun use 3.1.12 3.2.2 -- python app.py
    hrun use 3.1.12 3.2.2 -- time python app.py
    hrun use 3.1.12 3.2.2 -- python -m timeit app.py
    # discover case apps and run against versions
    hrun use 3.1.12 3.2.2 --case-dirs cases --entrypoint app.py
"""

import typer
from hrun.config import app as config_app
from hrun.run import app as run_app

app = typer.Typer(name="history-runner", no_args_is_help=True)
app.add_typer(config_app, name="config")
app.add_typer(run_app, name="run")


# Called before every command call

@app.callback()
def main():
    """
    history-runner is a tool for running a program (or program sets) across
    different versions (git tags or releases).
    """


if __name__ == "__main__":
    app()
