import os
import re

from config import code, load_config_yaml


class ProblemList:
    def __init__(self, file_path):
        self.src = "src"
        self.docs = "docs"
        self.data = load_config_yaml(
            os.path.join(self.src, "config", file_path)
        )
        self.dir = os.path.join(self.docs, self.data.dir)
        os.makedirs(self.dir, exist_ok=True)

        self.pattern = re.compile(r"^\d{4}_")

        # mkdocs
        self.tab = 4 * " "
        self.mkdocs_yaml = f"{self.tab}- {self.data.name}:\n"
        self.mkdocs_yaml += (
            f"{self.tab}{self.tab}- Home: {self.data.dir}/index.md\n"
        )

        # index
        self.index_md_path = os.path.join(self.docs, self.data.dir, "index.md")
        if not os.path.exists(self.index_md_path):
            with open(self.index_md_path, "w") as outfile:
                outfile.write(f"# {self.data.name}\n")

        for topic, problems in self.data.topics.items():
            self.generate_topic_markdown(topic, problems)

        print(self.mkdocs_yaml)

    def generate_topic_markdown(self, topic: str, problems, comments=True):
        files = [
            file
            for problem in problems
            for file in os.listdir(self.src)
            if file.endswith(".py")
            and self.pattern.match(file)
            and int(file.split("_")[0]) == problem
        ]

        title = f"# {topic}\n\n"
        md_name = topic.lower().replace(" ", "_") + ".md"
        md_path = os.path.join(self.docs, self.data.dir, md_name)

        self.mkdocs_yaml += (
            f"{self.tab}{self.tab}- {topic}: {self.data.dir}/{md_name}\n"
        )

        with open(md_path, "w") as outfile:
            outfile.write(f"---\ncomments: {comments}\n---\n\n")
            outfile.write(title)

            for file in files:
                filename = file.split(".")[0]
                md_file_path = os.path.join("docs", "md", filename + ".md")
                with open(md_file_path, "r") as infile:
                    data = infile.read()

                outfile.write(data + code(filename) + "\n")


if __name__ == "__main__":
    problems = os.listdir(os.path.join("src", "config"))
    for problem in problems:
        ProblemList(problem)
