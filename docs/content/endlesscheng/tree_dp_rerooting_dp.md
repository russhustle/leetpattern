---
comments: True
---

# Tree DP Rerooting DP

## Table of Contents

- [ ] [834. Sum of Distances in Tree](https://leetcode.cn/problems/sum-of-distances-in-tree/) (Hard)
- [ ] [2581. Count Number of Possible Root Nodes](https://leetcode.cn/problems/count-number-of-possible-root-nodes/) (Hard)
- [ ] [2858. Minimum Edge Reversals So Every Node Is Reachable](https://leetcode.cn/problems/minimum-edge-reversals-so-every-node-is-reachable/) (Hard)
- [x] [310. Minimum Height Trees](https://leetcode.cn/problems/minimum-height-trees/) (Medium)
- [ ] [3241. Time Taken to Mark All Nodes](https://leetcode.cn/problems/time-taken-to-mark-all-nodes/) (Hard)

## 834. Sum of Distances in Tree

-   [LeetCode](https://leetcode.com/problems/sum-of-distances-in-tree/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-distances-in-tree/) (Hard)

-   Tags: dynamic programming, tree, depth first search, graph

## 2581. Count Number of Possible Root Nodes

-   [LeetCode](https://leetcode.com/problems/count-number-of-possible-root-nodes/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-possible-root-nodes/) (Hard)

-   Tags: array, hash table, dynamic programming, tree, depth first search

## 2858. Minimum Edge Reversals So Every Node Is Reachable

-   [LeetCode](https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/) | [LeetCode CH](https://leetcode.cn/problems/minimum-edge-reversals-so-every-node-is-reachable/) (Hard)

-   Tags: dynamic programming, depth first search, breadth first search, graph

## 310. Minimum Height Trees

-   [LeetCode](https://leetcode.com/problems/minimum-height-trees/) | [LeetCode CH](https://leetcode.cn/problems/minimum-height-trees/) (Medium)

-   Tags: depth first search, breadth first search, graph, topological sort

```python title="310. Minimum Height Trees - Python Solution"
from collections import deque
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]

    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    q = deque([i for i in range(n) if len(graph[i]) == 1])
    remaining = n

    while remaining > 2:
        size = len(q)
        remaining -= size

        for _ in range(size):
            cur = q.popleft()
            nei = graph[cur].pop()
            graph[nei].remove(cur)

            if len(graph[nei]) == 1:
                q.append(nei)

    return list(q)


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(findMinHeightTrees(n, edges))  # [3, 4]

```

## 3241. Time Taken to Mark All Nodes

-   [LeetCode](https://leetcode.com/problems/time-taken-to-mark-all-nodes/) | [LeetCode CH](https://leetcode.cn/problems/time-taken-to-mark-all-nodes/) (Hard)

-   Tags: dynamic programming, tree, depth first search, graph
