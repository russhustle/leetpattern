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
            completed = file_not_empty(row["python_path"])
            completed = completed or file_not_empty(row["cpp_path"])
            progress = "x" if completed else " "
        elif category == "sql":
            progress = "x" if file_not_empty(row["sql_path"]) else " "
        content += (
            f"- [{progress}] [{row['QID']}. {row['title']}]({row['urlCh']})"
        )
        content += f" ({row['difficulty']})"
        content += " 👑\n" if row["paidOnly"] else "\n"
    return content + "\n"


def make_list_mkdocs(config_path):
    """Generate mkdocs list for the config."""
    cfg = load_config_yaml(os.path.join("config", config_path + ".yaml"))
    mkdocs = f"  - {cfg.name}:\n"
    mkdocs += f"    - Home: content/{cfg.dir}/index.md\n"
    for topic, _ in cfg.topics.items():
        md_path_name = topic.lower().replace(" ", "_") + ".md"
        mkdocs += f"    - {topic}: content/{cfg.dir}/{md_path_name}\n"
    return mkdocs


def make_list_index(config: str):
    """Generate index.md for the config.

    Args:
        config_path (str): Path to the config file.
    """
    cfg = load_config_yaml(os.path.join("config", config + ".yaml"))
    dir_md = os.path.join("docs", "content", "home", cfg.dir + ".md")
    index_md = os.path.join("docs", "content", cfg.dir, "index.md")

    if not os.path.exists(dir_md):
        comments = "---\ncomments: True\n---\n\n"
        with open(dir_md, "w") as f:
            f.write(comments + f"# {cfg.name}\n\n")

    with open(dir_md, "r") as f:
        content = f.read()

    with open(index_md, "w") as f:
        f.write(content)


def make_list_md(config_path):
    cfg = load_config_yaml(os.path.join("config", config_path + ".yaml"))
    folder = os.path.join("docs", "content", cfg.dir)
    df = pd.read_parquet(os.path.join("utils", "questions.parquet"))
    comments = "---\ncomments: True\n---\n\n"

    if not os.path.exists(folder):
        os.makedirs(folder)

    for topic, problems in cfg.topics.items():
        md_path_name = topic.lower().replace(" ", "_") + ".md"
        md_path = os.path.join(folder, md_path_name)

        content = comments
        content += f"# {topic}\n\n"
        content += topic_progress(df, problems, cfg.category)

        for idx in problems:
            row = df.loc[idx]

            # file checks
            check_make_file(row["md_path"])
            if cfg.category == "algorithms":
                check_make_file(row["python_path"])
                check_make_file(row["cpp_path"])
            elif cfg.category == "sql":
                check_make_file(row["sql_path"])
                check_make_file(row["txt_path"])

            content += row["markdown"]

            with open(row["md_path"], "r") as f:
                content += f.read() + "\n"

            content += code(cfg.category, row)

        with open(md_path, "w") as f:
            f.write(content)


def main():
    main_configuration = os.path.join("config", "main.yaml")
    default_mkdocs = os.path.join("utils", "mkdocs.yaml")
    output_mkdocs = os.path.join("mkdocs.yaml")

    with open(main_configuration, "r") as f:
        configs = yaml.safe_load(f)

    mkdocs = ""
    for config in configs:
        make_list_md(config)
        make_list_index(config)
        mkdocs += make_list_mkdocs(config) + "\n"

    # inset mkdocs into default_mkdocs line 3
    with open(default_mkdocs, "r") as f:
        lines = f.readlines()
        lines.insert(3, mkdocs)

    with open(output_mkdocs, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    # make_list_md("blind75")
    # make_list_index("blind75")
    # mkdocs = make_list_mkdocs("blind75")
    # print(mkdocs)
    main()
