import os
from dataclasses import dataclass, field
from typing import Dict, List

import pandas as pd
import yaml


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


def code(category, row) -> str:
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


def topic_progress(df, category, problems):
    content = ""
    for problem in problems:
        row = df.loc[problem]

        if category == "algorithms":
            py_path = os.path.join("src", row["basename"] + ".py")
            progress = "x" if not check_file_empty(py_path) else " "
        elif category == "sql":
            sql_path = os.path.join("src", "sql", row["basename"] + ".sql")
            progress = "x" if not check_file_empty(sql_path) else " "

        content += (
            f"- [{progress}] [{row['QID']}. {row['title']}]({row['urlCh']})"
        )
        content += f" ({row['difficulty']})\n"

    return content + "\n"


def check_make_file(file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")


def check_file_empty(file_path: str):
    with open(file_path, "r") as f:
        return f.read().strip() == ""


def create(config_path: str) -> str:
    cfg = load_config_yaml(os.path.join("config", config_path + ".yaml"))
    src = os.path.join("src")
    docs = os.path.join("docs")
    folder = os.path.join(docs, cfg.dir)
    if not os.path.exists(folder):
        os.makedirs(folder)

    comments = "---\ncomments: True\n---\n\n"

    # index.md
    index_md_path = os.path.join(folder, "index.md")
    if not os.path.exists(index_md_path):
        with open(index_md_path, "w") as f:
            f.write(comments + f"# {cfg.name}\n\n")

    df = pd.read_parquet(os.path.join("utils", "questions.parquet"))

    # mkdocs
    mkdocs = f"  - {cfg.name}:\n"
    mkdocs += f"    - Home: {cfg.dir}/index.md\n"

    for topic, problems in cfg.topics.items():
        md_path_name = topic.lower().replace(" ", "_") + ".md"
        md_path = os.path.join(folder, md_path_name)

        mkdocs += f"    - {topic}: {cfg.dir}/{md_path_name}\n"

        content = comments
        content += f"# {topic}\n\n"
        content += topic_progress(df, cfg.category, problems)
        problems = cfg.topics[topic]

        for idx in problems:
            row = df.loc[idx]

            # file checks
            problem_md_path = os.path.join(docs, "md", row["basename"] + ".md")
            check_make_file(problem_md_path)
            if cfg.category == "algorithms":
                problem_py_path = os.path.join(src, row["basename"] + ".py")
                check_make_file(problem_py_path)
            elif cfg.category == "sql":
                problem_sql_path = os.path.join(
                    src, "sql", row["basename"] + ".sql"
                )
                problem_txt_path = os.path.join(
                    src, "sql", row["basename"] + ".txt"
                )
                check_make_file(problem_sql_path)
                check_make_file(problem_txt_path)

            content += row["markdown"]
            with open(problem_md_path, "r") as f:
                content += f.read() + "\n"

            content += code(cfg.category, row)

        with open(md_path, "w") as f:
            f.write(content)

    return mkdocs


def main():
    main_configuration = os.path.join("config", "main.yaml")
    default_mkdocs = os.path.join("utils", "mkdocs.yaml")
    output_mkdocs = os.path.join("mkdocs.yaml")

    with open(main_configuration, "r") as file:
        configs = yaml.safe_load(file)

    mkdocs = ""
    for config in configs:
        mkdocs += create(config) + "\n"

    # inset mkdocs into default_mkdocs line 3
    with open(default_mkdocs, "r") as file:
        lines = file.readlines()
        lines.insert(3, mkdocs)

    with open(output_mkdocs, "w") as file:
        file.writelines(lines)


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


if __name__ == "__main__":
    main()
    # create_problem_files(2055)
