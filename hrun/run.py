"""Run command"""
import typer
app = typer.Typer(name="run", no_args_is_help=True)


@app.callback()
def run(command: str, tags: list[str]):
    """
    Run a command across different git tags
    """
    print(f"Running '{command}' across {tags}")
