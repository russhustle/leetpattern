"""Command line interface commands using Typer."""

import sys
from typing import Optional
import os
import typer

from .generator import DocumentationGenerator
from .problem import ProblemRepository
from .file_manager import FileManager

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

    file_manager = FileManager()

    file_manager.check_create_file(file_path)


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
