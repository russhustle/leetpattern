"""Problem domain models and repository."""

import os
from dataclasses import dataclass
from typing import List, Optional

import pandas as pd
from pandas import DataFrame


@dataclass
class Problem:
    """Represents a LeetCode problem with metadata and file paths."""

    qid: int
    title: str
    difficulty: str
    category: str
    url: str = ""
    url_ch: str = ""
    paid_only: bool = False
    python_path: Optional[str] = None
    cpp_path: Optional[str] = None
    javascript_path: Optional[str] = None
    sql_path: Optional[str] = None
    txt_path: Optional[str] = None
    md_path: Optional[str] = None
    basename: Optional[str] = None
    markdown: Optional[str] = None


class ProblemRepository:
    """Repository for managing problem data."""

    def __init__(self, data_path: str = "utils/questions.parquet"):
        self.data_path = data_path
        self._df: Optional[DataFrame] = None

    @property
    def df(self) -> DataFrame:
        """Lazy load the DataFrame."""
        if self._df is None:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(
                    f"Problem data file not found: {self.data_path}"
                )
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

    def get_problems(self, qids: List[int]) -> List[Problem]:
        """Get multiple problems by QID list."""
        problems = []
        for qid in qids:
            problem = self.get_problem(qid)
            if problem:
                problems.append(problem)
            else:
                print(f"Warning: Problem {qid} not found")
        return problems

    def get_problems_by_category(self, category: str) -> List[Problem]:
        """Get all problems in a specific category."""
        category_df = self.df[self.df["categorySlug"] == category]
        problems = []

        for index, row in category_df.iterrows():
            qid = (
                int(index)
                if isinstance(index, (int, float))
                else row.get("qid", index)
            )
            problem = self._row_to_problem(row, qid)
            if problem:
                problems.append(problem)

        return problems

    def _row_to_problem(self, row: pd.Series, qid: int) -> Problem:
        """Convert DataFrame row to Problem object."""
        sub_folder_index = (qid - 1) // 300
        start = sub_folder_index * 300 + 1
        end = (sub_folder_index + 1) * 300
        sub_folder = f"{start:04d}_{end:04d}"

        py_folder = f"leetpattern/solutions/python/{sub_folder}/"
        cpp_folder = f"leetpattern/solutions/cpp/{sub_folder}/"
        js_folder = f"leetpattern/solutions/javascript/{sub_folder}/"
        sql_folder = "leetpattern/solutions/sql/"

        basename = f"{qid:04d}_{row['titleSlug']}"

        python_path = f"{py_folder}{basename}.py"
        cpp_path = f"{cpp_folder}{basename}.cc"
        javascript_path = f"{js_folder}{basename}.js"
        sql_path = f"{sql_folder}{basename}.sql"

        return Problem(
            qid=qid,
            title=row.get("title", ""),
            difficulty=row.get("difficulty", ""),
            category=row.get("categorySlug", ""),
            url=row.get("url", ""),
            url_ch=row.get("urlCh", ""),
            paid_only=row.get("paidOnly", False),
            python_path=python_path,
            cpp_path=cpp_path,
            javascript_path=javascript_path,
            sql_path=sql_path,
            txt_path=row.get("txt_path"),
            md_path=row.get("md_path"),
            basename=basename,
            markdown=row.get("markdown"),
        )
