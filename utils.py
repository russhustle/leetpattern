from pandas import DataFrame
import os
from dataclasses import dataclass, field
from typing import Dict, List
import yaml
import pandas as pd


@dataclass
class Data:
    category: str
    dir: str
    name: str
    topics: Dict[str, List[int]] = field(default_factory=dict)


def load_config_yaml(file_path: str) -> Data:
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        return Data(**data)


def check_make_file(file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")


def check_file_empty(file_path: str):
    with open(file_path, "r") as f:
        return f.read().strip() == ""


def create_problem_files(qid: int):
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
        content = f'```python title="{title}"\n--8<-- "{basename}.py"\n```\n\n'
        return content if not check_file_empty(py_path) else "\n"

    elif category == "sql":
        txt_path = os.path.join("src", "sql", basename + ".txt")
        sql_path = os.path.join("src", "sql", basename + ".sql")
        txt = f'```txt title="{title}"\n--8<-- "sql/{basename}.txt"\n```\n\n'
        sql = f'```sql title="{title}"\n--8<-- "sql/{basename}.sql"\n```\n\n'
        content = ""
        content += txt if not check_file_empty(txt_path) else ""
        content += sql if not check_file_empty(sql_path) else ""
        return content
