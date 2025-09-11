import os
from typing import Optional

from .problem import Problem


def file_exists_and_not_empty(path: Optional[str]) -> bool:
    """Check if a file exists and is not empty."""
    if path is None:
        return False
    try:
        return os.path.isfile(path) and os.path.getsize(path) > 0
    except OSError:
        return False


class CodeExtractor:
    """Extracts and processes code content from solution files."""

    def __init__(self):
        pass

    def extract_code_content(self, problem: Problem) -> str:
        """Extract code content based on problem category."""
        if problem.category == "algorithms":
            return self.extract_algorithm_code(problem)
        elif problem.category == "sql":
            return self.extract_sql_code(problem)
        else:
            return ""

    def extract_algorithm_code(self, problem: Problem) -> str:
        """Extract code content for algorithm problems."""
        content = ""
        py_path = problem.python_path
        cpp_path = problem.cpp_path
        js_path = problem.javascript_path

        if py_path and file_exists_and_not_empty(py_path):
            content += (
                problem.py_snippet + "\n\n" if problem.py_snippet else ""
            )
        if cpp_path and file_exists_and_not_empty(cpp_path):
            content += (
                problem.cpp_snippet + "\n\n" if problem.cpp_snippet else ""
            )
        if js_path and file_exists_and_not_empty(js_path):
            content += (
                problem.js_snippet + "\n\n" if problem.js_snippet else ""
            )

        return content

    def extract_sql_code(self, problem: Problem) -> str:
        """Extract code content for SQL problems."""
        content = ""
        txt_path = problem.txt_path
        sql_path = problem.sql_path
        if txt_path and file_exists_and_not_empty(txt_path):
            content += (
                problem.txt_snippet + "\n\n" if problem.txt_snippet else ""
            )
        if sql_path and file_exists_and_not_empty(sql_path):
            content += (
                problem.sql_snippet + "\n\n" if problem.sql_snippet else ""
            )
        return content
