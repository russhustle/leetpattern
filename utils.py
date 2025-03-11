import os
from dataclasses import dataclass, field
from typing import Dict, List

import pandas as pd
import yaml
from pandas import DataFrame


@dataclass
class Data:
    category: str
    dir: str
    name: str
    topics: Dict[str, List[int]] = field(default_factory=dict)


def load_config_yaml(file_path: str) -> Data:
    """Load the configuration file"""
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        return Data(**data)


def check_make_file(file_path: str):
    """Create an empty file if it does not exist"""
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")


def file_not_empty(file_path: str):
    """Check if a file does not exist or is empty
    If the file does not exist, return False.
    If the file exists and is empty, return False.
    Otherwise, return True.
    """
    if not os.path.exists(file_path):
        return False
    return os.path.getsize(file_path) != 0


def create_problem_files(qid: int):
    """Create problem files for a given leetcode question ID"""
    df = pd.read_parquet(os.path.join("utils", "questions.parquet"))
    row = df.loc[qid]
    problem_md_path = os.path.join("docs", "md", row["basename"] + ".md")
    check_make_file(problem_md_path)

    if row["categorySlug"] == "algorithms":
        problem_py_path = os.path.join("src", row["basename"] + ".py")
        check_make_file(problem_py_path)
        print("created", problem_py_path)
    elif row["categorySlug"] == "database":
        problem_sql_path = os.path.join("src", "sql", row["basename"] + ".sql")
        problem_txt_path = os.path.join("src", "sql", row["basename"] + ".txt")
        check_make_file(problem_sql_path)
        check_make_file(problem_txt_path)
        print("created", problem_sql_path)


def code(category: str, row: DataFrame) -> str:
    """Code snippet for the problem"""
    basename = row["basename"]
    title = f"{row["QID"]}. {row["title"]}"

    if category == "algorithms":
        py_path = os.path.join("src", basename + ".py")
        cc_path = os.path.join("src", "cpp", basename + ".cc")

        py_content = f'```python title="{title} - Python Solution"\n--8<-- "{basename}.py"\n```\n\n'
        cc_content = f'```cpp title="{title} - C++ Solution"\n--8<-- "cpp/{basename}.cc"\n```\n\n'
        content = ""
        content += py_content if file_not_empty(py_path) else ""
        content += cc_content if file_not_empty(cc_path) else ""
        return content

    elif category == "sql":
        txt_path = os.path.join("src", "sql", basename + ".txt")
        sql_path = os.path.join("src", "sql", basename + ".sql")
        txt = f'```txt title="{title}"\n--8<-- "sql/{basename}.txt"\n```\n\n'
        sql = f'```sql title="{title}"\n--8<-- "sql/{basename}.sql"\n```\n\n'
        content = ""
        content += txt if file_not_empty(txt_path) else ""
        content += sql if file_not_empty(sql_path) else ""
        return content


def remove_empty_files():
    """Remove empty files"""
    folders = ["src", "docs/md", "src/sql"]
    for folder in folders:
        folder = os.path.join(os.getcwd(), folder)
        extensions = [".sql", ".py", ".txt", ".md"]
        py_filenames = [
            f for f in os.listdir(folder) if f.endswith(tuple(extensions))
        ]

        for py_filename in py_filenames:
            path = os.path.join(folder, py_filename)
            if os.path.getsize(path) == 0:
                os.remove(path)
                print(f"Removed {path}")
            else:
                print(f"Skipped {path}")
