---
comments: True
---

# Grid Applications

## Table of Contents

- [x] [1631. Path With Minimum Effort](https://leetcode.cn/problems/path-with-minimum-effort/) (Medium)
- [x] [778. Swim in Rising Water](https://leetcode.cn/problems/swim-in-rising-water/) (Hard)
- [x] [329. Longest Increasing Path in a Matrix](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) (Hard)
- [ ] [1036. Escape a Large Maze](https://leetcode.cn/problems/escape-a-large-maze/) (Hard)
- [x] [864. Shortest Path to Get All Keys](https://leetcode.cn/problems/shortest-path-to-get-all-keys/) (Hard)
- [ ] [1263. Minimum Moves to Move a Box to Their Target Location](https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/) (Hard)
- [ ] [2258. Escape the Spreading Fire](https://leetcode.cn/problems/escape-the-spreading-fire/) (Hard)
- [ ] [2556. Disconnect Path in a Binary Matrix by at Most One Flip](https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) (Medium)
- [ ] [2577. Minimum Time to Visit a Cell In a Grid](https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/) (Hard)
- [ ] [2617. Minimum Number of Visited Cells in a Grid](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/) (Hard)
- [x] [694. Number of Distinct Islands](https://leetcode.cn/problems/number-of-distinct-islands/) (Medium) 👑
- [ ] [711. Number of Distinct Islands II](https://leetcode.cn/problems/number-of-distinct-islands-ii/) (Hard) 👑
- [ ] [1102. Path With Maximum Minimum Value](https://leetcode.cn/problems/path-with-maximum-minimum-value/) (Medium) 👑

## 1631. Path With Minimum Effort

-   [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/) | [LeetCode CH](https://leetcode.cn/problems/path-with-minimum-effort/) (Medium)

-   Tags: array, binary search, depth first search, breadth first search, union find, heap priority queue, matrix
-   Return the minimum effort required to travel from the top-left to the bottom-right corner.

```python title="1631. Path With Minimum Effort - Python Solution"
import heapq
from typing import List


# Prim
def minimumEffortPath(heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(m)]
    heap = [(0, 0, 0)]  # (effort, row, col)

    while heap:
        effort, r, c = heapq.heappop(heap)

        if visited[r][c]:
            continue

        if r == m - 1 and c == n - 1:
            return effort

        visited[r][c] = True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                updated = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, (updated, nr, nc))

    return -1


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(minimumEffortPath(heights))  # 2

```

## 778. Swim in Rising Water

-   [LeetCode](https://leetcode.com/problems/swim-in-rising-water/) | [LeetCode CH](https://leetcode.cn/problems/swim-in-rising-water/) (Hard)

-   Tags: array, binary search, depth first search, breadth first search, union find, heap priority queue, matrix
-   Return the minimum time when you can reach the target.

![778](https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg)

```python title="778. Swim in Rising Water - Python Solution"
import heapq
from typing import List


# Dijkstra's
def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    visited = set()
    minHeap = [(grid[0][0], 0, 0)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited.add((0, 0))

    while minHeap:
        time, r, c = heapq.heappop(minHeap)

        if r == n - 1 and c == n - 1:
            return time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr in range(n) and nc in range(n) and (nr, nc) not in visited:
                visited.add((nr, nc))
                heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))


grid = [
    [0, 1, 2, 3, 4],
    [24, 23, 22, 21, 5],
    [12, 13, 14, 15, 16],
    [11, 17, 18, 19, 20],
    [10, 9, 8, 7, 6],
]
print(swimInWater(grid))  # 16

```

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

## 1036. Escape a Large Maze

-   [LeetCode](https://leetcode.com/problems/escape-a-large-maze/) | [LeetCode CH](https://leetcode.cn/problems/escape-a-large-maze/) (Hard)

-   Tags: array, hash table, depth first search, breadth first search
## 864. Shortest Path to Get All Keys

-   [LeetCode](https://leetcode.com/problems/shortest-path-to-get-all-keys/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-to-get-all-keys/) (Hard)

-   Tags: array, bit manipulation, breadth first search, matrix
```python title="864. Shortest Path to Get All Keys - Python Solution"
from collections import deque
from typing import List


# BFS
def shortestPathAllKeys(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    visited = set()
    total = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "@":
                q.append((r, c, 0, 0))
                visited.add((r, c, 0))
            if grid[r][c].islower():
                total += 1

    while q:
        r, c, keys, steps = q.popleft()

        if keys == (1 << total) - 1:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n:
                cell = grid[nr][nc]

                if cell == "#":
                    continue

                new_keys = keys
                if cell.islower():
                    new_keys |= 1 << (ord(cell) - ord("a"))

                if cell.isupper() and not (
                    keys & (1 << (ord(cell) - ord("A")))
                ):
                    continue

                if (nr, nc, new_keys) not in visited:
                    visited.add((nr, nc, new_keys))
                    q.append((nr, nc, new_keys, steps + 1))

    return -1


grid = ["@.a..", "###.#", "b.A.B"]
print(shortestPathAllKeys(grid))  # 8

```

## 1263. Minimum Moves to Move a Box to Their Target Location

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/) (Hard)

-   Tags: array, breadth first search, heap priority queue, matrix
## 2258. Escape the Spreading Fire

-   [LeetCode](https://leetcode.com/problems/escape-the-spreading-fire/) | [LeetCode CH](https://leetcode.cn/problems/escape-the-spreading-fire/) (Hard)

-   Tags: array, binary search, breadth first search, matrix
## 2556. Disconnect Path in a Binary Matrix by at Most One Flip

-   [LeetCode](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) | [LeetCode CH](https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) (Medium)

-   Tags: array, dynamic programming, depth first search, breadth first search, matrix
## 2577. Minimum Time to Visit a Cell In a Grid

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/) (Hard)

-   Tags: array, breadth first search, graph, heap priority queue, matrix, shortest path
## 2617. Minimum Number of Visited Cells in a Grid

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/) (Hard)

-   Tags: array, dynamic programming, stack, breadth first search, union find, heap priority queue, matrix, monotonic stack
## 694. Number of Distinct Islands

-   [LeetCode](https://leetcode.com/problems/number-of-distinct-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-distinct-islands/) (Medium)

-   Tags: hash table, depth first search, breadth first search, union find, hash function
```python title="694. Number of Distinct Islands - Python Solution"
from collections import deque
from copy import deepcopy
from typing import List


# BFS
def numDistinctIslandsBFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    shapes = set()
    dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    def bfs(r, c):
        q = deque([(r, c)])
        shape = set()
        grid[r][c] = 0

        while q:
            row, col = q.popleft()
            shape.add((row - r, col - c))

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 0

        return tuple(shape)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                shapes.add(bfs(i, j))

    return len(shapes)


# DFS
def numDistinctIslandsDFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(r, c, org, shape):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
            return

        grid[r][c] = 0
        shape.add((r - org[0], c - org[1]))

        dfs(r - 1, c, org, shape)
        dfs(r + 1, c, org, shape)
        dfs(r, c - 1, org, shape)
        dfs(r, c + 1, org, shape)

    shapes = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                org = [i, j]
                shape = set()
                dfs(i, j, org, shape)
                shapes.add(tuple(shape))

    return len(shapes)


grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
print(numDistinctIslandsBFS(deepcopy(grid)))  # 3
print(numDistinctIslandsDFS(deepcopy(grid)))  # 3

```

## 711. Number of Distinct Islands II

-   [LeetCode](https://leetcode.com/problems/number-of-distinct-islands-ii/) | [LeetCode CH](https://leetcode.cn/problems/number-of-distinct-islands-ii/) (Hard)

-   Tags: hash table, depth first search, breadth first search, union find, hash function
## 1102. Path With Maximum Minimum Value

-   [LeetCode](https://leetcode.com/problems/path-with-maximum-minimum-value/) | [LeetCode CH](https://leetcode.cn/problems/path-with-maximum-minimum-value/) (Medium)

-   Tags: array, binary search, depth first search, breadth first search, union find, heap priority queue, matrix
