---
comments: True
---

# Binary Search Minimize Max

## Table of Contents

- [ ] [410. Split Array Largest Sum](https://leetcode.cn/problems/split-array-largest-sum/) (Hard)
- [ ] [2064. Minimized Maximum of Products Distributed to Any Store](https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/) (Medium)
- [ ] [1760. Minimum Limit of Balls in a Bag](https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/) (Medium)
- [x] [1631. Path With Minimum Effort](https://leetcode.cn/problems/path-with-minimum-effort/) (Medium)
- [ ] [2439. Minimize Maximum of Array](https://leetcode.cn/problems/minimize-maximum-of-array/) (Medium)
- [ ] [2560. House Robber IV](https://leetcode.cn/problems/house-robber-iv/) (Medium)
- [x] [778. Swim in Rising Water](https://leetcode.cn/problems/swim-in-rising-water/) (Hard)
- [ ] [2616. Minimize the Maximum Difference of Pairs](https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/) (Medium)
- [ ] [3419. Minimize the Maximum Edge Weight of Graph](https://leetcode.cn/problems/minimize-the-maximum-edge-weight-of-graph/) (Medium)
- [ ] [2513. Minimize the Maximum of Two Arrays](https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/) (Medium)
- [ ] [3399. Smallest Substring With Identical Characters II](https://leetcode.cn/problems/smallest-substring-with-identical-characters-ii/) (Hard)
- [ ] [774. Minimize Max Distance to Gas Station](https://leetcode.cn/problems/minimize-max-distance-to-gas-station/) (Hard) 👑

## 410. Split Array Largest Sum

-   [LeetCode](https://leetcode.com/problems/split-array-largest-sum/) | [LeetCode CH](https://leetcode.cn/problems/split-array-largest-sum/) (Hard)

-   Tags: array, binary search, dynamic programming, greedy, prefix sum
## 2064. Minimized Maximum of Products Distributed to Any Store

-   [LeetCode](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) | [LeetCode CH](https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/) (Medium)

-   Tags: array, binary search, greedy
## 1760. Minimum Limit of Balls in a Bag

-   [LeetCode](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/) | [LeetCode CH](https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/) (Medium)

-   Tags: array, binary search
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

## 2439. Minimize Maximum of Array

-   [LeetCode](https://leetcode.com/problems/minimize-maximum-of-array/) | [LeetCode CH](https://leetcode.cn/problems/minimize-maximum-of-array/) (Medium)

-   Tags: array, binary search, dynamic programming, greedy, prefix sum
## 2560. House Robber IV

-   [LeetCode](https://leetcode.com/problems/house-robber-iv/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-iv/) (Medium)

-   Tags: array, binary search
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

## 2616. Minimize the Maximum Difference of Pairs

-   [LeetCode](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/) | [LeetCode CH](https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/) (Medium)

-   Tags: array, binary search, greedy
## 3419. Minimize the Maximum Edge Weight of Graph

-   [LeetCode](https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/) | [LeetCode CH](https://leetcode.cn/problems/minimize-the-maximum-edge-weight-of-graph/) (Medium)

-   Tags: binary search, depth first search, breadth first search, graph, shortest path
## 2513. Minimize the Maximum of Two Arrays

-   [LeetCode](https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/) | [LeetCode CH](https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/) (Medium)

-   Tags: math, binary search, number theory
## 3399. Smallest Substring With Identical Characters II

-   [LeetCode](https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/) | [LeetCode CH](https://leetcode.cn/problems/smallest-substring-with-identical-characters-ii/) (Hard)

-   Tags: string, binary search
## 774. Minimize Max Distance to Gas Station

-   [LeetCode](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) | [LeetCode CH](https://leetcode.cn/problems/minimize-max-distance-to-gas-station/) (Hard)

-   Tags: array, binary search
