---
comments: True
---

# Backtracking Combination

## Table of Contents

- [x] [77. Combinations](https://leetcode.cn/problems/combinations/) (Medium)
- [x] [216. Combination Sum III](https://leetcode.cn/problems/combination-sum-iii/) (Medium)
- [x] [22. Generate Parentheses](https://leetcode.cn/problems/generate-parentheses/) (Medium)
- [ ] [301. Remove Invalid Parentheses](https://leetcode.cn/problems/remove-invalid-parentheses/) (Hard)

## 77. Combinations

-   [LeetCode](https://leetcode.com/problems/combinations/) | [LeetCode CH](https://leetcode.cn/problems/combinations/) (Medium)

-   Tags: backtracking

```python title="77. Combinations - Python Solution"
import itertools
from typing import List


# Backtracking
def combine(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return None

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])

    return res


# itertools
def combineItertools(n: int, k: int) -> List[List[int]]:
    path = itertools.combinations(range(1, n + 1), k)
    return path


print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(list(combineItertools(4, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

```

## 216. Combination Sum III

-   [LeetCode](https://leetcode.com/problems/combination-sum-iii/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum-iii/) (Medium)

-   Tags: array, backtracking

```python title="216. Combination Sum III - Python Solution"
import itertools
from typing import List


# 1. Backtracking
def combinationSum3(k: int, n: int) -> List[List[int]]:
    path, result = [], []

    def backtracking(start):
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return

        for i in range(start, 10):
            path.append(i)
            backtracking(i + 1)
            path.pop()

    backtracking(1)

    return result


# 2. Itertools
def combinationSum3Itertools(k: int, n: int) -> List[List[int]]:
    combinations = itertools.combinations(range(1, 10), k)
    result = []

    for i in combinations:
        if sum(i) == n:
            result.append(i)

    return result


print(combinationSum3(3, 7))  # [[1, 2, 4]]
print(combinationSum3Itertools(3, 7))  # [(1, 2, 4)]

```

## 22. Generate Parentheses

-   [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)

-   Tags: string, dynamic programming, backtracking

```python title="22. Generate Parentheses - Python Solution"
from typing import List


# Backtracking
def generateParenthesis1(n: int) -> List[str]:
    path, res = [], []

    def dfs(openN, closeN):
        if openN == closeN == n:
            res.append("".join(path))
            return

        if openN < n:
            path.append("(")
            dfs(openN + 1, closeN)
            path.pop()

        if closeN < openN:
            path.append(")")
            dfs(openN, closeN + 1)
            path.pop()

    dfs(0, 0)

    return res


# Backtracking
def generateParenthesis2(n: int) -> List[str]:
    m = n * 2
    res, path = [], [""] * m

    def dfs(i, left):
        if i == m:
            res.append("".join(path))
            return

        if left < n:
            path[i] = "("
            dfs(i + 1, left + 1)
        if i - left < left:
            path[i] = ")"
            dfs(i + 1, left)

    dfs(0, 0)
    return res


if __name__ == "__main__":
    print(generateParenthesis1(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(generateParenthesis2(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']

```

## 301. Remove Invalid Parentheses

-   [LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/remove-invalid-parentheses/) (Hard)

-   Tags: string, backtracking, breadth first search
