---
name: solution-template
description: Generate LeetCode solution files using the Solution class template. Use when creating a new solution, refactoring an existing one to follow the standard structure, or scaffolding a problem file.
---

## Context

- Solutions live in `leetpattern/python/{range}/` as `{number}_{name}.py`
- Each file contains a `Solution` class with one method per approach
- Tests are inline at the bottom of the file
- Utility imports available: `from leetpattern.utils import LinkedList, ListNode, Trie, TrieNode, LPS`

## Template

```python
from typing import List


class Solution:
    def methodName(self, params) -> ReturnType:
        """Approach Name: O(?) time, O(?) space.
        Key insight or important point about this approach.
        """
        # implementation
        pass

    def methodNameAlt(self, params) -> ReturnType:
        """Approach Name: O(?) time, O(?) space.
        Key insight or important point about this approach.
        """
        # implementation
        pass


def test_method_name():
    s = Solution()
    for fn in (s.methodName, s.methodNameAlt):
        assert fn(input1) == expected1
        assert fn(input2) == expected2
        assert fn(edge_case) == edge_expected
```

## Rules

1. Use a single `Solution` class per file with one method per approach.
2. The optimal approach should be the first method in the class.
3. Each method must have a docstring with: approach name, time/space complexity, and the key insight that makes the approach work.
4. Method names use camelCase matching LeetCode's naming (e.g., `containsDuplicate`, `twoSum`).
5. Alternative approaches append a suffix: `methodNameSort`, `methodNameBF`, `methodNameDP`, etc.
6. The test function loops over all methods to verify they produce the same results.
7. Include at least 3 test cases: basic, non-trivial, and edge case (empty input, single element, etc.).
8. No module-level docstrings or headers. The docstrings on methods are sufficient documentation.
9. No `print()` calls or `if __name__` blocks. Use only the `test_` function.
10. Keep implementations minimal — no unnecessary variables or comments beyond the docstring.
11. Maximum line width is 90 characters. Wrap long docstrings, comments, and code to stay within this limit.
