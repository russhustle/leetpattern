"""Code extraction and processing utilities."""

from typing import Optional

from .file_manager import FileManager
from .problem import Problem


class CodeExtractor:
    """Extracts and processes code content from solution files."""

    def __init__(self):
        self.file_manager = FileManager()

    def extract_algorithm_code(self, problem: Problem) -> str:
        """Extract code content for algorithm problems."""
        content = ""
        title = f"{problem.qid}. {problem.title}"

        # Extract docstring from Python file if it exists
        if problem.python_path:
            py_docstring = self.file_manager.extract_docstring(
                problem.python_path
            )
            if py_docstring:
                content += py_docstring

        # Extract JSDoc comment from JavaScript file if it exists
        if problem.javascript_path:
            js_comment = self.file_manager.extract_js_comment(
                problem.javascript_path
            )
            if js_comment:
                content += js_comment

        # Add Python solution
        if (
            problem.python_path
            and self.file_manager.file_exists_and_not_empty(
                problem.python_path
            )
        ):
            py_content = self.file_manager.read_file_safe(
                problem.python_path
            ).strip()

            # Remove docstring from the code snippet if it exists
            if py_content.startswith('"""'):
                end_idx = py_content.find('"""', 3)
                if end_idx != -1:
                    py_content = py_content[end_idx + 3 :].strip()

            if py_content:  # Only add if there's actual code content
                py_content = f'```python title="{title} - Python Solution"\n{py_content}\n\n```\n\n'
                content += py_content

        # Add C++ solution
        if problem.cpp_path and self.file_manager.file_exists_and_not_empty(
            problem.cpp_path
        ):
            cc_content = self.file_manager.read_file_safe(problem.cpp_path)
            if cc_content.strip():  # Only add if there's actual code content
                cc_content = f'```cpp title="{title} - C++ Solution"\n{cc_content}```\n\n'
                content += cc_content

        # Add JavaScript solution
        if (
            problem.javascript_path
            and self.file_manager.file_exists_and_not_empty(
                problem.javascript_path
            )
        ):
            js_content = self.file_manager.read_file_safe(
                problem.javascript_path
            ).strip()

            # Remove JSDoc comment from the code snippet if it exists
            if js_content.startswith("/**"):
                end_idx = js_content.find("*/", 3)
                if end_idx != -1:
                    js_content = js_content[end_idx + 2 :].strip()

            if js_content:  # Only add if there's actual code content
                js_content = f'```javascript title="{title} - JavaScript Solution"\n{js_content}```\n\n'
                content += js_content

        return content

    def extract_sql_code(self, problem: Problem) -> str:
        """Extract code content for SQL problems."""
        content = ""
        title = f"{problem.qid}. {problem.title}"

        # Add problem description from txt file
        if problem.txt_path and self.file_manager.file_exists_and_not_empty(
            problem.txt_path
        ):
            basename = problem.basename or str(problem.qid)
            content += f'```txt title="{title}"\n--8<-- "solutions/sql/{basename}.txt"\n```\n\n'

        # Add SQL solution
        if problem.sql_path and self.file_manager.file_exists_and_not_empty(
            problem.sql_path
        ):
            basename = problem.basename or str(problem.qid)
            content += f'```sql title="{title}"\n--8<-- "solutions/sql/{basename}.sql"\n```\n\n'

        return content

    def extract_code_content(self, problem: Problem) -> str:
        """Extract code content based on problem category."""
        if problem.category == "algorithms":
            return self.extract_algorithm_code(problem)
        elif problem.category == "sql":
            return self.extract_sql_code(problem)
        else:
            return ""
