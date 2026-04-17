---
name: test-gen
description: Generate pytest-discoverable unit tests for LeetCode solution files. Use when adding tests to a solution, converting bare asserts to test functions, or creating test cases for a problem.
---

## Context

- Solutions live in `leetpattern/python/{range}/` as `{number}_{name}.py`
- Tests are inline in the same solution file (no separate test files)
- pytest discovers `def test_*` functions in files matching `[0-9][0-9][0-9][0-9]_*.py`
- Utility imports available: `from leetpattern.utils import LinkedList, ListNode, Trie, TrieNode, LPS`

## Test Format

Append a `def test_<function_name>():` function at the bottom of the solution file. Each test function should contain multiple assert statements covering different cases.

```python
def test_<function_name>():
    # basic cases
    assert <function_name>(<input>) == <expected>
    # edge cases
    assert <function_name>(<edge_input>) == <edge_expected>
```

## Rules

1. The test function name must start with `test_` followed by the solution function name (snake_case).
2. Include at least 3 test cases: a basic case, an edge case (empty input, single element, etc.), and a non-trivial case.
3. If the solution uses a class with multiple methods (e.g., `longestPalindrome.dp`), create one test function per method: `def test_<class>_<method>():`.
4. For linked list problems, use `LinkedList` and `ListNode` from `leetpattern.utils` for construction and comparison.
5. For tree problems, use `binarytree` or the project's tree utilities for construction.
6. If the file already has bare `assert` statements or `if __name__` blocks with test logic, convert them into proper `def test_*` functions and remove the old code.
7. Do not add duplicate test functions if a valid `def test_*` already exists — extend it instead.
8. Keep test cases concise. Use inline values, not fixtures.
9. If a problem has multiple valid outputs (e.g., "return any valid answer"), use `assert result in [<valid1>, <valid2>]` or `assert sorted(result) == sorted(expected)`.
10. Add the LeetCode problem URL as a comment above the test function: `# https://leetcode.com/problems/<slug>/`.
