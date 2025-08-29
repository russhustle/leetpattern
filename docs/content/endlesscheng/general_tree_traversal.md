---
comments: True
---

# General Tree Traversal

## Table of Contents

- [ ] [2368. Reachable Nodes With Restrictions](https://leetcode.cn/problems/reachable-nodes-with-restrictions/) (Medium)
- [x] [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)
- [x] [582. Kill Process](https://leetcode.cn/problems/kill-process/) (Medium) 👑

## 2368. Reachable Nodes With Restrictions

-   [LeetCode](https://leetcode.com/problems/reachable-nodes-with-restrictions/) | [LeetCode CH](https://leetcode.cn/problems/reachable-nodes-with-restrictions/) (Medium)

-   Tags: array, hash table, tree, depth first search, breadth first search, union find, graph
## 1466. Reorder Routes to Make All Paths Lead to the City Zero

-   [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [LeetCode CH](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)

-   Tags: depth first search, breadth first search, graph
-   ![1466](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

```python title="1466. Reorder Routes to Make All Paths Lead to the City Zero - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def minReorderBFS(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))  # go
        graph[v].append((u, 0))  # come

    changes = 0
    q = deque([(0, -1)])

    while q:
        n1, d1 = q.popleft()

        for n2, d2 in graph[n1]:
            if n2 != d1:
                changes += d2
                q.append((n2, n1))

    return changes


# DFS
def minReorderDFS(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))  # go
        graph[v].append((u, 0))  # come

    def dfs(n1, d1):
        changes = 0
        for n2, d2 in graph[n1]:
            if n2 != d1:
                changes += d2 + dfs(n2, n1)
        return changes

    return dfs(0, -1)


n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
print(minReorderBFS(n, connections))  # 2
print(minReorderDFS(n, connections))  # 2

```

## 582. Kill Process

-   [LeetCode](https://leetcode.com/problems/kill-process/) | [LeetCode CH](https://leetcode.cn/problems/kill-process/) (Medium)

-   Tags: array, hash table, tree, depth first search, breadth first search
```python title="582. Kill Process - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def killProcess(pid: List[int], ppid: List[int], kill: int) -> List[int]:
    graph = defaultdict(list)

    for u, v in zip(ppid, pid):
        graph[u].append(v)

    q = deque([kill])
    res = []

    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in graph[cur]:
            q.append(nxt)

    return res


if __name__ == "__main__":
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    assert killProcess(pid, ppid, kill) == [5, 10]

```
