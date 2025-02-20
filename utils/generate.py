import os
import re

code = (
    lambda filename: f"""
=== "Python"

    ```python
    --8<-- "{filename}.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/{filename}.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/{filename}.ts"
    ```
"""
)


def generate_markdown(output: str):
    path = "src"
    pattern = re.compile(r"^\d{4}_")
    files = sorted(
        [f for f in os.listdir(path) if f.endswith(".py") and pattern.match(f)]
    )

    title = "# LeetPattern\n\n"

    with open(os.path.join("docs", output + ".md"), "w") as outfile:
        outfile.write(title)

        for file in files:
            filename = file.split(".")[0]
            md_file_path = os.path.join("docs", "md", filename + ".md")
            with open(md_file_path, "r") as infile:
                data = infile.read()

            outfile.write(data + code(filename))
            outfile.write("\n")


if __name__ == "__main__":
    generate_markdown("all")
