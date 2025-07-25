---
comments: True
---

# DP Grid Advanced

## Table of Contents

- [ ] [1594. Maximum Non Negative Product in a Matrix](https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/) (Medium)
- [ ] [1301. Number of Paths with Max Score](https://leetcode.cn/problems/number-of-paths-with-max-score/) (Hard)
- [ ] [2435. Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) (Hard)
- [ ] [174. Dungeon Game](https://leetcode.cn/problems/dungeon-game/) (Hard)
- [x] [329. Longest Increasing Path in a Matrix](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) (Hard)
- [ ] [2328. Number of Increasing Paths in a Grid](https://leetcode.cn/problems/number-of-increasing-paths-in-a-grid/) (Hard)
- [ ] [2267.  Check if There Is a Valid Parentheses String Path](https://leetcode.cn/problems/check-if-there-is-a-valid-parentheses-string-path/) (Hard)
- [ ] [1937. Maximum Number of Points with Cost](https://leetcode.cn/problems/maximum-number-of-points-with-cost/) (Medium)
- [ ] [3363. Find the Maximum Number of Fruits Collected](https://leetcode.cn/problems/find-the-maximum-number-of-fruits-collected/) (Hard)
- [ ] [1463. Cherry Pickup II](https://leetcode.cn/problems/cherry-pickup-ii/) (Hard)
- [ ] [741. Cherry Pickup](https://leetcode.cn/problems/cherry-pickup/) (Hard)
- [ ] [3459. Length of Longest V-Shaped Diagonal Segment](https://leetcode.cn/problems/length-of-longest-v-shaped-diagonal-segment/) (Hard)
- [ ] [2510. Check if There is a Path With Equal Number of 0's And 1's](https://leetcode.cn/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) (Medium) 👑

## 1594. Maximum Non Negative Product in a Matrix

-   [LeetCode](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/) | [LeetCode CH](https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/) (Medium)

-   Tags: array, dynamic programming, matrix
## 1301. Number of Paths with Max Score

-   [LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/) | [LeetCode CH](https://leetcode.cn/problems/number-of-paths-with-max-score/) (Hard)

-   Tags: array, dynamic programming, matrix
## 2435. Paths in Matrix Whose Sum Is Divisible by K

-   [LeetCode](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) | [LeetCode CH](https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) (Hard)

-   Tags: array, dynamic programming, matrix
## 174. Dungeon Game

-   [LeetCode](https://leetcode.com/problems/dungeon-game/) | [LeetCode CH](https://leetcode.cn/problems/dungeon-game/) (Hard)

-   Tags: array, dynamic programming, matrix
## 329. Longest Increasing Path in a Matrix

-   [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) (Hard)

-   Tags: array, dynamic programming, depth first search, breadth first search, graph, topological sort, memoization, matrix

```python title="329. Longest Increasing Path in a Matrix - Python Solution"
from collections import deque
from functools import cache
from typing import List


# BFS - Topological Sort
def longestIncreasingPathBFS(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Calculate indegrees and initialize queue in one pass
    indegree = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and matrix[nr][nc] > matrix[i][j]
                ):
                    indegree[nr][nc] += 1

    # Start with cells that have no smaller neighbors
    queue = deque(
        (i, j) for i in range(m) for j in range(n) if indegree[i][j] == 0
    )

    res = 0
    while queue:
        res += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        queue.append((nr, nc))

    return res


# DP - 2D
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @cache
    def dfs(r, c):
        path = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                path = max(path, dfs(nr, nc) + 1)
        return path

    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))

    return res


if __name__ == "__main__":
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert longestIncreasingPath(matrix) == 4
    assert longestIncreasingPathBFS(matrix) == 4

```

## 2328. Number of Increasing Paths in a Grid

-   [LeetCode](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/number-of-increasing-paths-in-a-grid/) (Hard)

-   Tags: array, dynamic programming, depth first search, breadth first search, graph, topological sort, memoization, matrix
## 2267.  Check if There Is a Valid Parentheses String Path

-   [LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/) | [LeetCode CH](https://leetcode.cn/problems/check-if-there-is-a-valid-parentheses-string-path/) (Hard)

-   Tags: array, dynamic programming, matrix
## 1937. Maximum Number of Points with Cost

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-points-with-cost/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-points-with-cost/) (Medium)

-   Tags: array, dynamic programming, matrix
## 3363. Find the Maximum Number of Fruits Collected

-   [LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/) | [LeetCode CH](https://leetcode.cn/problems/find-the-maximum-number-of-fruits-collected/) (Hard)

-   Tags: array, dynamic programming, matrix
## 1463. Cherry Pickup II

-   [LeetCode](https://leetcode.com/problems/cherry-pickup-ii/) | [LeetCode CH](https://leetcode.cn/problems/cherry-pickup-ii/) (Hard)

-   Tags: array, dynamic programming, matrix
## 741. Cherry Pickup

-   [LeetCode](https://leetcode.com/problems/cherry-pickup/) | [LeetCode CH](https://leetcode.cn/problems/cherry-pickup/) (Hard)

-   Tags: array, dynamic programming, matrix
## 3459. Length of Longest V-Shaped Diagonal Segment

-   [LeetCode](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/) | [LeetCode CH](https://leetcode.cn/problems/length-of-longest-v-shaped-diagonal-segment/) (Hard)

-   Tags: array, dynamic programming, memoization, matrix
## 2510. Check if There is a Path With Equal Number of 0's And 1's

-   [LeetCode](https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) | [LeetCode CH](https://leetcode.cn/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) (Medium)

-   Tags: array, dynamic programming, matrix
