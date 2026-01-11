import os
from dataclasses import dataclass
from typing import Optional

import pandas as pd
from pandas import DataFrame


def if_file_exist(path: str) -> bool:
    return os.path.exists(path) and os.path.getsize(path) > 0


@dataclass
class Problem:
    """Represents a LeetCode problem with metadata and file paths."""

    qid: int
    title: str
    difficulty: str
    category: str
    url: str = ""
    url_ch: str = ""
    urls_for_md: str = ""
    tags: str = ""
    paid_only: bool = False
    is_done: bool = False

    progress: str = ""
    heading: str = ""

    basename: Optional[str] = None
    markdown: Optional[str] = None
    sub_folder: Optional[str] = None
    # paths
    py_path: Optional[str] = None
    cpp_path: Optional[str] = None
    js_path: Optional[str] = None
    sql_path: Optional[str] = None
    txt_path: Optional[str] = None
    md_path: Optional[str] = None

    # Code snippets for different languages
    py_snippet: Optional[str] = None
    cpp_snippet: Optional[str] = None
    js_snippet: Optional[str] = None
    sql_snippet: Optional[str] = None
    txt_snippet: Optional[str] = None


class ProblemRepository:
    """Repository for managing problem data."""

    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            data_path = os.path.join(os.path.dirname(__file__), "questions.parquet")
        self.data_path = data_path
        self._df: Optional[DataFrame] = None

    @property
    def df(self) -> DataFrame:
        """Lazy load the DataFrame."""
        if self._df is None:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Problem data file not found: {self.data_path}")
            self._df = pd.read_parquet(self.data_path)
        return self._df

    def get_problem(self, qid: int) -> Optional[Problem]:
        """Get a single problem by QID."""
        try:
            row = self.df.loc[qid]
            # handle case where multiple rows match
            if isinstance(row, pd.DataFrame):
                row = row.iloc[0]
            return self._row_to_problem(row, qid)
        except KeyError:
            return None

    def _row_to_problem(self, row: pd.Series, qid: int) -> Problem:
        """Convert DataFrame row to Problem object."""
        sub_folder_index = (qid - 1) // 300
        start = sub_folder_index * 300 + 1
        end = (sub_folder_index + 1) * 300
        sub_folder = f"{start:04d}_{end:04d}"

        py_folder = f"leetpattern/python/{sub_folder}/"
        cpp_folder = f"leetpattern/cpp/{sub_folder}/"
        js_folder = f"leetpattern/javascript/{sub_folder}/"
        sql_folder = "leetpattern/sql/"

        basename = f"{qid:04d}_{row['titleSlug']}"

        python_path = f"{py_folder}{basename}.py"
        cpp_path = f"{cpp_folder}{basename}.cc"
        javascript_path = f"{js_folder}{basename}.js"
        sql_path = f"{sql_folder}{basename}.sql"
        txt_path = f"{sql_folder}{basename}.txt"

        urls_for_md = f"-    [LeetCode]({row['url']}) | [力扣]({row['urlCh']})"

        # check if any of the code files exist
        is_done = False
        if if_file_exist(python_path):
            is_done = True
        if if_file_exist(cpp_path):
            is_done = True
        if if_file_exist(javascript_path):
            is_done = True
        if if_file_exist(sql_path):
            is_done = True
        heading = f"## {qid}. {row['title'] + (" 👑" if row['paidOnly'] else "")}"
        heading_link = f"#{qid}-{row['titleSlug'].replace('_', '-')}"
        progress = f"- [{"x" if is_done else " "}] [{qid}. {row['title']}]({heading_link}) ({row['difficulty']})"
        progress += f"{" 👑" if row['paidOnly'] else ""}"
        tags = f"-   Tags: {row['topicTags'].title() if row['topicTags'] else 'None'}"

        return Problem(
            qid=qid,
            title=row.get("title", ""),
            difficulty=row.get("difficulty", ""),
            category=row.get("categorySlug", ""),
            url=row.get("url", ""),
            url_ch=row.get("urlCh", ""),
            urls_for_md=urls_for_md,
            paid_only=row.get("paidOnly", False),
            sub_folder=sub_folder,
            py_path=python_path,
            cpp_path=cpp_path,
            js_path=javascript_path,
            sql_path=sql_path,
            txt_path=txt_path,
            md_path=row.get("md_path"),
            basename=basename,
            markdown=row.get("markdown"),
            heading=heading,
            is_done=is_done,
            progress=progress,
            tags=tags,
            # code snippets
            py_snippet=(
                snippet("Python", f"python/{sub_folder}/{basename}.py")
                if if_file_exist(python_path)
                else ""
            ),
            cpp_snippet=(
                snippet("CPP", f"cpp/{sub_folder}/{basename}.cc")
                if if_file_exist(cpp_path)
                else ""
            ),
            js_snippet=(
                snippet("JavaScript", f"javascript/{sub_folder}/{basename}.js")
                if if_file_exist(javascript_path)
                else ""
            ),
            sql_snippet=(
                snippet("SQL", f"sql/{basename}.sql") if if_file_exist(sql_path) else ""
            ),
            txt_snippet=(
                snippet("TXT", f"sql/{basename}.txt") if if_file_exist(txt_path) else ""
            ),
        )


def snippet(lang, path):
    content = f"""=== "{lang}"

    ```{lang.lower()}
    --8<-- "{path}"
    ```
"""
    return content
