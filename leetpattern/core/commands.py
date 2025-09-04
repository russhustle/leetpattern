"""Command line interface commands using Typer."""

import os
import sys
from typing import Optional

import typer

from .file_manager import FileManager
from .generator import DocumentationGenerator
from .problem import ProblemRepository

app = typer.Typer(
    name="leetpattern",
    help="LeetPattern - Documentation generator for LeetCode patterns",
)


@app.command()
def generate(
    config_dir: str = typer.Option(
        "config",
        "--config-dir",
        help="Directory containing configuration files",
    ),
    config: Optional[str] = typer.Option(
        None,
        "--config",
        help="Generate documentation for specific config only",
    ),
) -> None:
    """Generate documentation."""
    generator = DocumentationGenerator(config_dir)

    if config:
        success = generator.generate_single_config(config)
    else:
        success = generator.generate_all_configs()

    if not success:
        typer.echo("Documentation generation failed", err=True)
        raise typer.Exit(1)

    typer.echo("Documentation generated successfully!")


@app.command()
def create(
    qid: int,
    language: str = typer.Option(
        "py", "--lang", help="Programming language (py, cc, sql)"
    ),
) -> None:
    """Create problem files."""
    problem = ProblemRepository().get_problem(qid)
    if not problem:
        typer.echo(f"Problem {qid} not found", err=True)
        raise typer.Exit(1)

    # Validate language option
    valid_languages = {"py", "cc", "sql"}
    if language not in valid_languages:
        typer.echo(
            f"Invalid language '{language}'. Valid options: {', '.join(valid_languages)}",
            err=True,
        )
        raise typer.Exit(1)

    # Generate different file paths based on language
    if language == "py":
        file_path = problem.python_path
    elif language == "cc":
        file_path = problem.cpp_path
    elif language == "sql":
        file_path = problem.sql_path
    else:
        # This should be unreachable due to validation above, but let's be explicit
        typer.echo(
            f"Invalid language '{language}'. Valid options: {', '.join(valid_languages)}",
            err=True,
        )
        raise typer.Exit(1)

    if not file_path:
        typer.echo(
            f"No file path available for problem {qid} in language {language}",
            err=True,
        )
        raise typer.Exit(1)

    file_manager = FileManager()
    file_manager.check_create_file(file_path)


@app.command()
def show(
    qid: int,
    language: str = typer.Option(
        "py", "--lang", help="Programming language (py, cc, sql)"
    ),
):
    """Show problem files."""
    problem = ProblemRepository().get_problem(qid)

    if not problem:
        typer.echo(f"Problem {qid} not found", err=True)
        raise typer.Exit(1)

    if language == "py":
        file_path = problem.python_path
    elif language == "cc":
        file_path = problem.cpp_path
    elif language == "sql":
        file_path = problem.sql_path
    else:
        typer.echo(
            f"Invalid language '{language}'. Valid options: py, cc, sql",
            err=True,
        )
        raise typer.Exit(1)

    # print the file content
    if file_path and os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
            typer.echo(content)
            typer.echo(f"\n{file_path}")
    else:
        typer.echo(
            f"File for Problem {qid} ({language}) not found or doesn't exist: {file_path}",
            err=True,
        )


def main() -> int:
    """Main CLI entry point."""
    try:
        app()
        return 0
    except typer.Exit as e:
        return e.exit_code
    except KeyboardInterrupt:
        typer.echo("\nOperation cancelled by user", err=True)
        return 1
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
