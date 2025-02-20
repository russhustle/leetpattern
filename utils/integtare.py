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

        for topic, problems in self.data.topics.items():
            self.generate_topic_markdown(topic, problems)

    def generate_topic_markdown(self, topic, problems, comments=True):
        if problems:
            files = [
                file
                for problem in problems
                for file in os.listdir(self.src)
                if file.endswith(".py")
                and self.pattern.match(file)
                and int(file.split("_")[0]) == problem
            ]
        else:
            files = sorted(
                [
                    file
                    for file in os.listdir(self.src)
                    if file.endswith(".py") and self.pattern.match(file)
                ]
            )

        title = f"# {topic}\n\n"
        md_path = os.path.join(
            self.docs, self.data.dir, topic.lower().replace(" ", "_") + ".md"
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
