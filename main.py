import os
from typing import List

import pandas as pd
import yaml
from pandas import DataFrame

from utils import check_make_file, code, file_not_empty, load_config_yaml


def topic_progress(
    df: DataFrame, problems: List[int], category: str = "algorithms"
):
    """Generate a ist of problems with progress.

    Args:
        df (DataFrame): DataFrame containing the questions
        problems (List[int]): List of questions
        category (str, optional): Category of the questions. Defaults to "algorithms", "sql".

    Returns:
        str: List of problems with progress.
    """
    content = ""
    for problem in problems:
        row = df.loc[problem]

        if category == "algorithms":
            py_path = os.path.join("src", row["basename"] + ".py")
            cc_path = os.path.join("src", "cpp", row["basename"] + ".cc")
            completed = file_not_empty(py_path) or file_not_empty(cc_path)
            progress = "x" if completed else " "

        elif category == "sql":
            sql_path = os.path.join("src", "sql", row["basename"] + ".sql")
            progress = "x" if file_not_empty(sql_path) else " "

        content += (
            f"- [{progress}] [{row['QID']}. {row['title']}]({row['urlCh']})"
        )
        content += f" ({row['difficulty']})"
        content += " 👑\n" if row["paidOnly"] else "\n"

    return content + "\n"


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
        content += topic_progress(df, problems, cfg.category)
        problems = cfg.topics[topic]

        for idx in problems:
            row = df.loc[idx]

            # file checks
            problem_md_path = os.path.join(docs, "md", row["basename"] + ".md")
            check_make_file(problem_md_path)
            if cfg.category == "algorithms":
                problem_py_path = os.path.join(src, row["basename"] + ".py")
                problem_cc_path = os.path.join(
                    src, "cpp", row["basename"] + ".cc"
                )
                check_make_file(problem_py_path)
                check_make_file(problem_cc_path)
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


if __name__ == "__main__":
    main()
