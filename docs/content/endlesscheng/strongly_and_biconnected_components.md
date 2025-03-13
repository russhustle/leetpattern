---
comments: True
---

# Strongly and Biconnected Components

- [x] [1192. Critical Connections in a Network](https://leetcode.cn/problems/critical-connections-in-a-network/) (Hard)
- [ ] [1568. Minimum Number of Days to Disconnect Island](https://leetcode.cn/problems/minimum-number-of-days-to-disconnect-island/) (Hard)
- [ ] [3383. Minimum Runes to Add to Cast Spell](https://leetcode.cn/problems/minimum-runes-to-add-to-cast-spell/) (Hard) 👑

## 1192. Critical Connections in a Network

-   [LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/) | [LeetCode CH](https://leetcode.cn/problems/critical-connections-in-a-network/) (Hard)

-   Tags: depth first search, graph, biconnected component

```python title="1192. Critical Connections in a Network - Python Solution"
from collections import defaultdict
from typing import List


# Tarjan
def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    bridges = []
    time = 0

    def dfs(n1, prev):
        nonlocal time
        disc[n1], low[n1] = time, time
        time += 1

        for n2 in graph[n1]:
            if n2 == prev:
                continue
            if disc[n2] == -1:
                dfs(n2, n1)
                low[n1] = min(low[n1], low[n2])

                if low[n2] > disc[n1]:
                    bridges.append([n1, n2])
            else:
                low[n1] = min(low[n1], disc[n2])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return bridges


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(criticalConnections(n, connections))  # [[1, 3]]

```

## 1568. Minimum Number of Days to Disconnect Island

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-days-to-disconnect-island/) (Hard)

-   Tags: array, depth first search, breadth first search, matrix, strongly connected component

## 3383. Minimum Runes to Add to Cast Spell

-   [LeetCode](https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/) | [LeetCode CH](https://leetcode.cn/problems/minimum-runes-to-add-to-cast-spell/) (Hard)

-   Tags: array, depth first search, breadth first search, union find, graph, topological sort
