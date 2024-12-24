from typing import List


def complexity(table: List[List[str]]) -> None:
    header = ["Approach", "Time", "Space"]
    table.insert(0, header)

    col_widths = [
        max(len(row[i]) for row in table) for i in range(len(table[0]))
    ]

    def format_row(row):
        return " | ".join(
            f"{cell:<{col_widths[i]}}" for i, cell in enumerate(row)
        )

    separator = "|".join("-" * (width + 2) for width in col_widths)

    print(f"# |{separator}|")
    print(f"# | {format_row(table[0])} |")
    print(f"# |{separator}|")
    for row in table[1:]:
        print(f"# | {format_row(row)} |")
    print(f"# |{separator}|")
