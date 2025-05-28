---
comments: True
---

# General Tree Diameter

## Table of Contents

- [ ] [2246. Longest Path With Different Adjacent Characters](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/) (Hard)
- [ ] [3203. Find Minimum Diameter After Merging Two Trees](https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/) (Hard)
- [ ] [1617. Count Subtrees With Max Distance Between Cities](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/) (Hard)
- [ ] [2538. Difference Between Maximum and Minimum Price Sum](https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/) (Hard)
- [x] [1245. Tree Diameter](https://leetcode.cn/problems/tree-diameter/) (Medium) 👑
- [ ] [3313. Find the Last Marked Nodes in Tree](https://leetcode.cn/problems/find-the-last-marked-nodes-in-tree/) (Hard) 👑

## 2246. Longest Path With Different Adjacent Characters

-   [LeetCode](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/) (Hard)

-   Tags: array, string, tree, depth first search, graph, topological sort
## 3203. Find Minimum Diameter After Merging Two Trees

-   [LeetCode](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/) | [LeetCode CH](https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/) (Hard)

-   Tags: tree, depth first search, breadth first search, graph
## 1617. Count Subtrees With Max Distance Between Cities

-   [LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) | [LeetCode CH](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/) (Hard)

-   Tags: dynamic programming, bit manipulation, tree, enumeration, bitmask
## 2538. Difference Between Maximum and Minimum Price Sum

-   [LeetCode](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) | [LeetCode CH](https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/) (Hard)

-   Tags: array, dynamic programming, tree, depth first search
## 1245. Tree Diameter

-   [LeetCode](https://leetcode.com/problems/tree-diameter/) | [LeetCode CH](https://leetcode.cn/problems/tree-diameter/) (Medium)

-   Tags: tree, depth first search, breadth first search, graph, topological sort

```python title="1245. Tree Diameter - Python Solution"
from collections import defaultdict, deque
from typing import List


# Tree Diameter
def treeDiameter(edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {0}
    q = deque([0])
    cur = 0

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)

    visited = {cur}
    q = deque([cur])
    res = -1

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
        res += 1

    return res


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
assert treeDiameter(edges) == 4

```

## 3313. Find the Last Marked Nodes in Tree

-   [LeetCode](https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-the-last-marked-nodes-in-tree/) (Hard)

-   Tags: tree, depth first search
