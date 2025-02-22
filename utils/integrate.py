import argparse
import os
import re

import pandas as pd

from config import code, load_config_yaml, sql_code


class ProblemList:
    def __init__(self, file: str):
        self.src = "src"
        self.docs = "docs"
        self.df = pd.read_parquet(os.path.join("utils", "questions.parquet"))
        self.cfg = load_config_yaml(os.path.join(self.src, "config", file))
        self.dir = os.path.join(self.docs, self.cfg.dir)
        os.makedirs(self.dir, exist_ok=True)

        # index
        self.index_md_path = os.path.join(self.docs, self.cfg.dir, "index.md")
        if not os.path.exists(self.index_md_path):
            with open(self.index_md_path, "w") as outfile:
                outfile.write(f"# {self.cfg.name}\n")

        self.pattern = re.compile(r"^\d{4}_")

        # mkdocs
        self.mkdocs_yaml = f"- {self.cfg.name}:\n"
        self.mkdocs_yaml += f"  - Home: {self.cfg.dir}/index.md\n"

        for topic, problems in self.cfg.topics.items():
            self.generate_topic_markdown(topic, problems)

    def generate_topic_markdown(self, topic: str, problems, comments=True):
        title = f"# {topic}\n\n"
        md_name = topic.lower().replace(" ", "_") + ".md"
        md_path = os.path.join(self.docs, self.cfg.dir, md_name)

        self.mkdocs_yaml += f"  - {topic}: {self.cfg.dir}/{md_name}\n"

        with open(md_path, "w") as outfile:
            outfile.write(f"---\ncomments: {comments}\n---\n\n")
            outfile.write(title)

            for qid in problems:
                content = self.problem_markdown(qid)
                outfile.write(content)

    def problem_markdown(self, qid: int):
        row = self.df[self.df.QID == qid]
        name = row["titleSlug"].values[0]
        basename = str(qid).zfill(4) + "_" + name
        filename = os.path.join(self.dir, basename + ".md")

        if os.path.exists(filename):
            with open(filename, "r") as infile:
                content = infile.read()
                content += code(basename) + "\n"
        else:
            content = row["markdown"].values[0]
            with open(filename, "w") as f:
                f.write(content + "\n")

        return content


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--file_path", "-f", type=str, help="Path to the yaml file"
    # )
    # args = parser.parse_args()

    # ProblemList(args.file_path)
    problems = os.listdir(os.path.join("src", "config"))
    for problem in problems:
        ProblemList(problem)
