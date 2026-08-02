---
name: solution-template
description: Use when generating or refactoring LeetCode Python solution files in this repo, including normal Solution-class problems and design problems that must keep the original judged class name.
---

## Shape

- Files live in `leetpattern/python/{range}/{number}_{name}.py`.
- Use `Solution` for normal algorithm problems.
- For design problems, keep the original LeetCode class name and API exactly
  (`KthLargest`, `LRUCache`, `MedianFinder`, etc.). Do not wrap it in
  `Solution`.
- Put pytest-style inline tests at the bottom.

## Algorithm Skeleton

```python
class Solution:
    def methodName(self, args) -> ReturnType:
        """Approach Name: O(?) time, O(?) space.
        Key insight.
        """
        ...


def test_method_name():
    s = Solution()
    for fn in (s.methodName,):
        assert fn(case) == expected
```

## Design Skeleton

```python
class OriginalClassName:
    def __init__(self, args):
        """Setup Approach: O(?) time, O(?) space.
        Key state invariant.
        """
        ...

    def requiredMethod(self, args) -> ReturnType:
        """Operation Approach: O(?) time, O(?) space.
        Key update/query invariant.
        """
        ...


def test_original_class_name():
    obj = OriginalClassName(init_args)
    assert obj.requiredMethod(case) == expected
```

## Rules

1. Put the optimal approach first.
2. Use camelCase names matching LeetCode. Alternative algorithm methods may add a
   suffix such as `Sort`, `BF`, or `DP`.
3. Add docstrings to public solution methods. For design problems, document
   `__init__` and judged public operations.
4. Include at least 3 useful test cases, including an edge case.
5. Use only `test_` functions: no module headers, `print()`, or `if __name__`
   blocks.
6. Keep code minimal and lines at 90 characters or less.
