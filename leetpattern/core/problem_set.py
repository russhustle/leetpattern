from dataclasses import dataclass, field
from pathlib import Path
import yaml

from leetpattern import Topic, TopicRepository


@dataclass
class ProblemSet:
    name: str = ""
    dir_name: str = ""
    category: str = ""
    topics: list[Topic] = field(default_factory=list)


class ProblemSetRepository:
    def __init__(self, config_path: str, folder: str = "temp"):
        self.problem_set = ProblemSet()
        self.load_yaml(config_path)
        self.folder = Path(folder)
        self.problem_set_folder = self.folder / self.problem_set.dir_name
        self.docs = self.problem_set_folder / "docs"

    def load_yaml(self, config_path: str) -> None:
        """Read YAML at config_path and populate ProblemSet.topics."""
        path = Path(config_path)
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        self.problem_set.name = data.get("name", "")
        self.problem_set.dir_name = data.get("dir", "")
        self.problem_set.category = data.get("category", "")
        topics = data.get("topics", {})
        if not isinstance(topics, dict):
            raise ValueError("topics should be a dict of topic names to problem IDs")
        for topic_name, problem_ids in topics.items():
            topic = Topic(
                config_dir=self.problem_set.dir_name,
                name=topic_name,
                problem_ids=tuple(problem_ids),
            )
            repo = TopicRepository(topic)
            self.problem_set.topics.append(repo.topic)

    def make_topics_md(self):
        for topic in self.problem_set.topics:
            topic_path = self.docs / topic.md_path
            topic_path.parent.mkdir(parents=True, exist_ok=True)
            with topic_path.open("w", encoding="utf-8") as file:
                file.write(topic.md_content)

    def make_readme_md(self):
        content = f"# {self.problem_set.name}\n\n"
        readme_path = self.docs / "README.md"
        with readme_path.open("w", encoding="utf-8") as file:
            file.write(content)

    def make_mkdocs_yaml(self):
        content = f"site_name: {self.problem_set.name}\n\nnav:\n"
        for topic in self.problem_set.topics:
            mkdocs_content = f"- {topic.name}: {topic.md_path}\n"
            content += mkdocs_content
        mkdocs_path = self.problem_set_folder / "mkdocs.yaml"
        with mkdocs_path.open("w", encoding="utf-8") as file:
            file.write(content)


if __name__ == "__main__":
    paths = ["config/blind75.yaml", "config/grind75.yaml", "config/sql50.yaml"]
    for path in paths:
        repo = ProblemSetRepository(path)
        repo.make_topics_md()
        repo.make_readme_md()
        repo.make_mkdocs_yaml()
