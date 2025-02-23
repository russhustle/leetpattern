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


def code(category, basename):
    if category == "algorithms":
        return f'```python\n--8<-- "{basename}.py"\n```'
    elif category == "sql":
        return f"""```txt\n--8<-- "sql/{basename}.txt"\n```\n```sql\n--8<-- "sql/{basename}.sql"\n```\n"""


def check_make_file(file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")


def create(config_path: str) -> str:
    cfg = load_config_yaml(os.path.join("config", config_path + ".yaml"))
    src = os.path.join("src")
    docs = os.path.join("docs")
    folder = os.path.join(docs, cfg.dir)
    if not os.path.exists(folder):
        os.makedirs(folder)
    index_md_path = os.path.join(folder, "index.md")
    if not os.path.exists(index_md_path):
        with open(index_md_path, "w") as f:
            f.write(f"# {cfg.name}\n\n")

    df = pd.read_parquet(os.path.join("utils", "questions.parquet"))

    mkdocs = f"  - {cfg.name}:\n"
    mkdocs += f"    - Home: {cfg.dir}/index.md\n"

    for topic, problems in cfg.topics.items():
        md_path_name = topic.lower().replace(" ", "_") + ".md"
        md_path = os.path.join(folder, md_path_name)

        mkdocs += f"    - {topic}: {cfg.dir}/{md_path_name}\n"

        content = "---\ncomments: True\n---\n\n"
        content += f"# {topic}\n\n"
        problems = cfg.topics[topic]

        for idx in problems:

            row = df.loc[idx]
            problem_md_path = os.path.join(docs, "md", row["basename"] + ".md")

            content += row["markdown"]

            if os.path.exists(problem_md_path):
                with open(problem_md_path, "r") as f:
                    content += f.read() + "\n"
            else:
                with open(problem_md_path, "w") as f:
                    f.write("")

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

            content += code(cfg.category, row["basename"]) + "\n\n"

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


if __name__ == "__main__":
    main()
