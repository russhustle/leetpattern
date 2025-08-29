"""Command line interface commands."""

import argparse
import sys

from ..core.generator import DocumentationGenerator


def generate_docs(args) -> int:
    """Generate documentation command."""
    generator = DocumentationGenerator(args.config_dir)

    if args.config:
        success = generator.generate_single_config(args.config)
    else:
        success = generator.generate_all_configs()

    return 0 if success else 1


def create_problem(args) -> int:
    """Create problem files command (disabled)."""
    print("Auto file creation is disabled.")
    print("Please create problem files manually if needed.")
    return 0


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="LeetPattern - Documentation generator for LeetCode patterns"
    )
    parser.add_argument(
        "--config-dir",
        default="config",
        help="Directory containing configuration files",
    )

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands"
    )

    # Generate documentation command
    gen_parser = subparsers.add_parser(
        "generate", help="Generate documentation"
    )
    gen_parser.add_argument(
        "--config", help="Generate documentation for specific config only"
    )
    gen_parser.set_defaults(func=generate_docs)

    # Create problem files command (disabled)
    create_parser = subparsers.add_parser(
        "create", help="Create problem files (disabled)"
    )
    create_parser.add_argument("qid", type=int, help="Problem QID")
    create_parser.set_defaults(func=create_problem)

    # Parse arguments
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return 1

    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
