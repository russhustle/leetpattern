from dataclasses import dataclass

from leetpattern import ProblemRepository


@dataclass
class Topic:
    config_dir: str = ""
    name: str = ""
    problem_ids: tuple[int, ...] = tuple()

    md_content: str = ""
    md_path: str = ""
    mkdocs_path: str = ""


class TopicRepository:
    def __init__(self, topic: Topic):
        self.topic = topic
        # md_content
        md_content = self.comments(comments=True) + "\n"
        md_content += f"# {self.topic.name}\n\n"
        md_content += self.toc() + "\n\n"
        for qid in self.topic.problem_ids:
            md_content += self.problem_content(qid) + "\n\n"
        self.topic.md_content = md_content

        # md_path
        self.topic.md_path = self.topic.name.lower().replace(" ", "_") + ".md"

    def comments(self, comments: bool) -> str:
        return f"""---
comments: {comments}
---
"""

    def toc(self):
        toc = "## Table of Contents\n\n"
        for qid in self.topic.problem_ids:
            problem = ProblemRepository().get_problem(qid)
            toc += problem.progress + "\n" if problem else ""
        return toc

    def problem_content(self, qid: int) -> str:
        problem = ProblemRepository().get_problem(qid)
        content = problem.heading + "\n\n" if problem else ""
        content += problem.urls_for_md + "\n\n" if problem else ""
        content += problem.tags + "\n\n" if problem else ""
        if problem and problem.category == "algorithms":
            content += problem.py_snippet + "\n" if problem.py_snippet else ""
            content += problem.cpp_snippet + "\n" if problem.cpp_snippet else ""
            content += problem.js_snippet + "\n" if problem.js_snippet else ""
        elif problem and problem.category == "database":
            content += problem.txt_snippet + "\n" if problem.txt_snippet else ""
            content += problem.sql_snippet + "\n" if problem.sql_snippet else ""

        return content


if __name__ == "__main__":
    topic = Topic(
        config_dir="blind75",
        name="Array",
        problem_ids=(1, 2, 3, 4, 5),
    )
    repo = TopicRepository(topic)
    from pprint import pprint

    pprint(repo.topic)
