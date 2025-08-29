---
comments: True
---

# Backtracking

## Table of Contents

- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)
- [x] [79. Word Search](https://leetcode.cn/problems/word-search/) (Medium)

## 39. Combination Sum

-   [LeetCode](https://leetcode.com/problems/combination-sum/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum/) (Medium)

-   Tags: array, backtracking
```python title="39. Combination Sum - Python Solution"
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)
    res, path = [], []

    def dfs(total, start):
        if total > target:
            return
        if total == target:
            res.append(path.copy())
            return

        for i in range(start, n):
            total += candidates[i]
            path.append(candidates[i])
            dfs(total, i)
            total -= candidates[i]
            path.pop()

    dfs(0, 0)

    return res


if __name__ == "__main__":
    print(combinationSum([2, 3, 5], 8))
    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(combinationSum([2, 3, 6, 7], 7))
    # [[2, 2, 3], [7]]

```

## 79. Word Search

-   [LeetCode](https://leetcode.com/problems/word-search/) | [LeetCode CH](https://leetcode.cn/problems/word-search/) (Medium)

-   Tags: array, string, backtracking, depth first search, matrix
```python title="79. Word Search - Python Solution"
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    path = set()
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (
            r < 0
            or r >= m
            or c < 0
            or c >= n
            or board[r][c] != word[i]
            or (r, c) in path
        ):
            return False

        path.add((r, c))

        for dr, dc in dirs:
            if dfs(r + dr, c + dc, i + 1):
                return True

        path.remove((r, c))
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
word = "ABCCED"
print(exist(board, word))  # True

```

