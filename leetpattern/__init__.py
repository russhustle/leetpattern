"""LeetPattern - Documentation generator for LeetCode problem patterns."""

__version__ = "0.3.0"
__author__ = "Sihan A"


# from .core.generator import DocumentationGenerator
from .core.problem import Problem, ProblemRepository
from .core.topic import Topic, TopicRepository
from .core.problem_set import ProblemSet, ProblemSetRepository

__all__ = [
    "Problem",
    "ProblemRepository",
    "Topic",
    "TopicRepository",
    "ProblemSet",
    "ProblemSetRepository",
]
