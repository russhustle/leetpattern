"""Command line interface commands using Typer."""

import sys
from typing import Optional

import typer

from ..core.generator import DocumentationGenerator

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
def create(qid: int) -> None:
    """Create problem files (disabled)."""
    typer.echo("Auto file creation is disabled.")
    typer.echo("Please create problem files manually if needed.")


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
