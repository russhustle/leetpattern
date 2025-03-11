---
comments: True
---

# Reverse Thinking

- [ ] [2139. Minimum Moves to Reach Target Score](https://leetcode.cn/problems/minimum-moves-to-reach-target-score/) (Medium)
- [ ] [1558. Minimum Numbers of Function Calls to Make Target Array](https://leetcode.cn/problems/minimum-numbers-of-function-calls-to-make-target-array/) (Medium)
- [ ] [554. Brick Wall](https://leetcode.cn/problems/brick-wall/) (Medium)
- [ ] [2718. Sum of Matrix After Queries](https://leetcode.cn/problems/sum-of-matrix-after-queries/) (Medium)
- [x] [417. Pacific Atlantic Water Flow](https://leetcode.cn/problems/pacific-atlantic-water-flow/) (Medium)
- [ ] [991. Broken Calculator](https://leetcode.cn/problems/broken-calculator/) (Medium)
- [ ] [2227. Encrypt and Decrypt Strings](https://leetcode.cn/problems/encrypt-and-decrypt-strings/) (Hard)
- [ ] [3419. Minimize the Maximum Edge Weight of Graph](https://leetcode.cn/problems/minimize-the-maximum-edge-weight-of-graph/) (Medium)
- [ ] [936. Stamping The Sequence](https://leetcode.cn/problems/stamping-the-sequence/) (Hard)

## 2139. Minimum Moves to Reach Target Score

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-score/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-reach-target-score/) (Medium)

-   Tags: math, greedy

## 1558. Minimum Numbers of Function Calls to Make Target Array

-   [LeetCode](https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-numbers-of-function-calls-to-make-target-array/) (Medium)

-   Tags: array, greedy, bit manipulation

## 554. Brick Wall

-   [LeetCode](https://leetcode.com/problems/brick-wall/) | [LeetCode CH](https://leetcode.cn/problems/brick-wall/) (Medium)

-   Tags: array, hash table

## 2718. Sum of Matrix After Queries

-   [LeetCode](https://leetcode.com/problems/sum-of-matrix-after-queries/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-matrix-after-queries/) (Medium)

-   Tags: array, hash table

## 417. Pacific Atlantic Water Flow

-   [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [LeetCode CH](https://leetcode.cn/problems/pacific-atlantic-water-flow/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix

```python title="417. Pacific Atlantic Water Flow - Python Solution"
from collections import deque
from typing import List


# DFS
def pacificAtlanticDFS(heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(r, c, visited, prev_height):
        if (
            r not in range(m)
            or c not in range(n)
            or heights[r][c] < prev_height
            or (r, c) in visited
        ):
            return None

        visited.add((r, c))
        height = heights[r][c]
        for dr, dc in directions:
            dfs(dr + r, dc + c, visited, height)

    for c in range(n):
        dfs(0, c, pac, heights[0][c])
        dfs(m - 1, c, atl, heights[m - 1][c])

    for r in range(m):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, n - 1, atl, heights[r][n - 1])

    return list(pac & atl)


# BFS
def pacificAtlanticBFS(heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c, visited):
        q = deque([(r, c)])
        visited.add((r, c))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (
                    nr in range(m)
                    and nc in range(n)
                    and heights[row][col] <= heights[nr][nc]
                    and (nr, nc) not in visited
                ):
                    q.append((nr, nc))
                    visited.add((nr, nc))

    for c in range(n):
        bfs(0, c, pac)  # top
        bfs(m - 1, c, atl)  # bottom

    for r in range(m):
        bfs(r, 0, pac)  # left
        bfs(r, n - 1, atl)  # right

    return list(pac & atl)


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacificAtlanticDFS(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
print(pacificAtlanticBFS(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]

```

## 991. Broken Calculator

-   [LeetCode](https://leetcode.com/problems/broken-calculator/) | [LeetCode CH](https://leetcode.cn/problems/broken-calculator/) (Medium)

-   Tags: math, greedy

## 2227. Encrypt and Decrypt Strings

-   [LeetCode](https://leetcode.com/problems/encrypt-and-decrypt-strings/) | [LeetCode CH](https://leetcode.cn/problems/encrypt-and-decrypt-strings/) (Hard)

-   Tags: array, hash table, string, design, trie

## 3419. Minimize the Maximum Edge Weight of Graph

-   [LeetCode](https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/) | [LeetCode CH](https://leetcode.cn/problems/minimize-the-maximum-edge-weight-of-graph/) (Medium)

-   Tags: binary search, depth first search, breadth first search, graph, shortest path

## 936. Stamping The Sequence

-   [LeetCode](https://leetcode.com/problems/stamping-the-sequence/) | [LeetCode CH](https://leetcode.cn/problems/stamping-the-sequence/) (Hard)

-   Tags: string, stack, greedy, queue
