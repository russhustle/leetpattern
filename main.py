#!/usr/bin/env python3
"""LeetPattern - Documentation generator for LeetCode problem patterns.

This is the main entry point for the LeetPattern application.
Use the CLI interface for all operations.

Usage:
    python main.py generate [--config CONFIG_NAME]
    python main.py create QID  # (disabled)

Examples:
    python main.py generate                    # Generate all configs
    python main.py generate --config blind75   # Generate specific config
"""

import sys
from leetpattern.leetpattern.cli.commands import main

if __name__ == "__main__":
    sys.exit(main())