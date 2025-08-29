---
comments: True
---

# General Tree Topological Sort

## Table of Contents

- [x] [310. Minimum Height Trees](https://leetcode.cn/problems/minimum-height-trees/) (Medium)
- [ ] [2603. Collect Coins in a Tree](https://leetcode.cn/problems/collect-coins-in-a-tree/) (Hard)

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

## 2603. Collect Coins in a Tree

-   [LeetCode](https://leetcode.com/problems/collect-coins-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/collect-coins-in-a-tree/) (Hard)

-   Tags: array, tree, graph, topological sort
