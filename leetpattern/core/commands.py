from pathlib import Path

import typer

from leetpattern import ProblemRepository

app = typer.Typer()


@app.command()
def show(
    qid: int = typer.Argument(..., help="LeetCode question ID"),
    lang: str = typer.Option("py", "--lang", "-l", help="Programming language"),
):
    """
    Show the written code for a given question ID and programming language.
    """
    pr = ProblemRepository()
    problem = pr.get_problem(qid)

    if not problem:
        typer.echo(f"Problem with ID {qid} not found.")
        raise typer.Exit(code=1)

    path = ""
    if lang == "py":
        path = problem.py_path
    elif lang == "cpp":
        path = problem.cpp_path
    elif lang == "js":
        path = problem.js_path
    elif lang == "sql":
        path = problem.sql_path

    if path and Path(path).exists():
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            typer.echo(content + "\n")
            typer.echo(f"File path: {path}")

    else:
        typer.echo(f"No file found for question ID {qid} in {lang}.")


@app.command()
def create(
    qid: int = typer.Argument(..., help="LeetCode question ID"),
    lang: str = typer.Option("py", "--lang", "-l", help="Programming language"),
):
    """
    Create a new code file for a given question ID and programming language.
    """
    pr = ProblemRepository()
    problem = pr.get_problem(qid)

    if not problem:
        typer.echo(f"Problem with ID {qid} not found.")
        raise typer.Exit(code=1)

    path = ""
    if lang == "py":
        path = problem.py_path
    elif lang == "cpp":
        path = problem.cpp_path
    elif lang == "js":
        path = problem.js_path
    elif lang == "sql":
        path = problem.sql_path

    if path and Path(path).exists():
        typer.echo(f"File already exists for question ID {qid} in {lang}: {path}")
        raise typer.Exit(code=1)

    if path:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            file.write(f"# Solution for {problem.title} (ID: {qid})\n")
        typer.echo(f"Created new file: {path}")
    else:
        typer.echo(f"Unsupported language: {lang}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
