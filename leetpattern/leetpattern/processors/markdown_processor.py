"""Markdown content generation and processing."""

import os
from typing import List

from ..core.config import Config
from ..core.problem import Problem, ProblemRepository
from ..io.file_manager import FileManager
from .code_extractor import CodeExtractor


class MarkdownProcessor:
    """Processes and generates markdown content."""
    
    def __init__(self):
        self.file_manager = FileManager()
        self.code_extractor = CodeExtractor()
        self.problem_repo = ProblemRepository()
    
    def generate_problem_progress(self, problems: List[Problem], category: str = "algorithms") -> str:
        """Generate a list of problems with progress indicators."""
        content = "## Table of Contents\n\n"
        
        for problem in problems:
            if category == "algorithms":
                py_completed = problem.python_path and self.file_manager.file_exists_and_not_empty(problem.python_path)
                cpp_completed = problem.cpp_path and self.file_manager.file_exists_and_not_empty(problem.cpp_path)
                completed = py_completed or cpp_completed
            elif category == "sql":
                completed = problem.sql_path and self.file_manager.file_exists_and_not_empty(problem.sql_path)
            else:
                completed = False
            
            progress = "x" if completed else " "
            content += f"- [{progress}] [{problem.qid}. {problem.title}]({problem.url_ch})"
            content += f" ({problem.difficulty})"
            content += " 👑\n" if problem.paid_only else "\n"
        
        return content + "\n"
    
    def generate_topic_content(self, config: Config, topic: str, problem_qids: List[int]) -> str:
        """Generate complete content for a topic markdown file."""
        problems = self.problem_repo.get_problems(problem_qids)
        
        content = "---\ncomments: True\n---\n\n"
        content += f"# {topic}\n\n"
        content += self.generate_problem_progress(problems, config.category)
        
        for problem in problems:
            # Add problem's existing markdown content if available
            if problem.markdown:
                content += problem.markdown
            
            # Add code content
            code_content = self.code_extractor.extract_code_content(problem)
            content += code_content
        
        return content
    
    def create_topic_file(self, config: Config, topic: str, problem_qids: List[int]) -> bool:
        """Create a markdown file for a specific topic."""
        folder = os.path.join("docs", "content", config.dir)
        os.makedirs(folder, exist_ok=True)
        
        md_filename = topic.lower().replace(" ", "_") + ".md"
        md_path = os.path.join(folder, md_filename)
        
        content = self.generate_topic_content(config, topic, problem_qids)
        return self.file_manager.write_file_safe(md_path, content)
    
    def create_index_file(self, config: Config) -> bool:
        """Create index.md file for the configuration."""
        home_md = os.path.join("docs", "content", "home", config.dir + ".md")
        index_md = os.path.join("docs", "content", config.dir, "index.md")
        
        # Create home file if it doesn't exist
        if not os.path.exists(home_md):
            comments = "---\ncomments: True\n---\n\n"
            content = comments + f"# {config.name}\n\n"
            self.file_manager.write_file_safe(home_md, content)
        
        # Copy content from home to index
        home_content = self.file_manager.read_file_safe(home_md)
        return self.file_manager.write_file_safe(index_md, home_content)