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
    url_ch: str = ""
    paid_only: bool = False
    python_path: Optional[str] = None
    cpp_path: Optional[str] = None
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
                raise FileNotFoundError(f"Problem data file not found: {self.data_path}")
            self._df = pd.read_parquet(self.data_path)
        return self._df
    
    def get_problem(self, qid: int) -> Optional[Problem]:
        """Get a single problem by QID."""
        try:
            row = self.df.loc[qid]
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
        category_df = self.df[self.df['categorySlug'] == category]
        problems = []
        
        for qid, row in category_df.iterrows():
            problem = self._row_to_problem(row, qid)
            if problem:
                problems.append(problem)
                
        return problems
    
    def _row_to_problem(self, row: pd.Series, qid: int) -> Problem:
        """Convert DataFrame row to Problem object."""
        # Update file paths to match new structure
        python_path = row.get('python_path')
        if python_path:
            python_path = python_path.replace('src/python/', 'leetpattern/solutions/python/')
            
        cpp_path = row.get('cpp_path')
        if cpp_path:
            cpp_path = cpp_path.replace('src/cpp/', 'leetpattern/solutions/cpp/')
            
        sql_path = row.get('sql_path') 
        if sql_path:
            sql_path = sql_path.replace('src/sql/', 'leetpattern/solutions/sql/')
            
        return Problem(
            qid=qid,
            title=row.get('title', ''),
            difficulty=row.get('difficulty', ''),
            category=row.get('categorySlug', ''),
            url_ch=row.get('urlCh', ''),
            paid_only=row.get('paidOnly', False),
            python_path=python_path,
            cpp_path=cpp_path, 
            sql_path=sql_path,
            txt_path=row.get('txt_path'),
            md_path=row.get('md_path'),
            basename=row.get('basename'),
            markdown=row.get('markdown')
        )