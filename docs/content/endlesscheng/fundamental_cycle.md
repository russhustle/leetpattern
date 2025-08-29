---
comments: True
---

# Fundamental Cycle

## Table of Contents

- [ ] [2359. Find Closest Node to Given Two Nodes](https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/) (Medium)
- [x] [2360. Longest Cycle in a Graph](https://leetcode.cn/problems/longest-cycle-in-a-graph/) (Hard)
- [x] [684. Redundant Connection](https://leetcode.cn/problems/redundant-connection/) (Medium)
- [x] [685. Redundant Connection II](https://leetcode.cn/problems/redundant-connection-ii/) (Hard)
- [ ] [2876. Count Visited Nodes in a Directed Graph](https://leetcode.cn/problems/count-visited-nodes-in-a-directed-graph/) (Hard)
- [ ] [2127. Maximum Employees to Be Invited to a Meeting](https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/) (Hard)
- [ ] [2836. Maximize Value of Function in a Ball Passing Game](https://leetcode.cn/problems/maximize-value-of-function-in-a-ball-passing-game/) (Hard)
- [ ] [2204. Distance to a Cycle in Undirected Graph](https://leetcode.cn/problems/distance-to-a-cycle-in-undirected-graph/) (Hard) 👑

## 2359. Find Closest Node to Given Two Nodes

-   [LeetCode](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/) | [LeetCode CH](https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/) (Medium)

-   Tags: depth first search, graph
## 2360. Longest Cycle in a Graph

-   [LeetCode](https://leetcode.com/problems/longest-cycle-in-a-graph/) | [LeetCode CH](https://leetcode.cn/problems/longest-cycle-in-a-graph/) (Hard)

-   Tags: depth first search, breadth first search, graph, topological sort
```python title="2360. Longest Cycle in a Graph - Python Solution"
from typing import List


def longestCycle(edges: List[int]) -> int:
    n = len(edges)
    res = -1
    cur = 1
    vis = [0 for _ in range(n)]

    for i in range(n):
        start = cur
        while i != -1 and vis[i] == 0:
            vis[i] = cur
            cur += 1
            i = edges[i]
        if i != -1 and vis[i] >= start:
            res = max(res, cur - vis[i])

    return res


if __name__ == "__main__":
    edges = [3, 3, 4, 2, 3]
    print(longestCycle(edges))  # 3

```

## 684. Redundant Connection

-   [LeetCode](https://leetcode.com/problems/redundant-connection/) | [LeetCode CH](https://leetcode.cn/problems/redundant-connection/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
```python title="684. Redundant Connection - Python Solution"
from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}
        self.rank = {i: 1 for i in range(1, n + 1)}

    def find(self, n):
        p = self.par[n]
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True


# Union Find
def findRedundantConnectionUF(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n)

    for u, v in edges:
        if not uf.union(u, v):
            return (u, v)


# DFS
def findRedundantConnectionDFS(edges: List[List[int]]) -> List[int]:
    graph, cycle = {}, {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    def dfs(node, parent):
        if node in cycle:
            for k in list(cycle.keys()):
                if k == node:
                    return True
                del cycle[k]

        cycle[node] = None
        for child in graph[node]:
            if child != parent and dfs(child, node):
                return True
        del cycle[node]
        return False

    dfs(edges[0][0], -1)
    for a, b in edges[::-1]:
        if a in cycle and b in cycle:
            return (a, b)


edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantConnectionUF(edges))  # (2, 3)
print(findRedundantConnectionDFS(edges))  # (2, 3)

```

## 685. Redundant Connection II

-   [LeetCode](https://leetcode.com/problems/redundant-connection-ii/) | [LeetCode CH](https://leetcode.cn/problems/redundant-connection-ii/) (Hard)

-   Tags: depth first search, breadth first search, union find, graph
```python title="685. Redundant Connection II - Python Solution"
from typing import List


# Union Find
def findRedundantDirectedConnectionUF(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n + 1)
    parent = list(range(n + 1))
    candidates = []

    for u, v in edges:
        if parent[v] != v:
            candidates.append([parent[v], v])
            candidates.append([u, v])
        else:
            parent[v] = u

    if not candidates:
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]

    for u, v in edges:
        if [u, v] == candidates[1]:
            continue
        if not uf.union(u, v):
            return candidates[0]

    return candidates[1]


class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        self.par[p1] = p2
        return True


edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantDirectedConnectionUF(edges))

```

## 2876. Count Visited Nodes in a Directed Graph

-   [LeetCode](https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/) | [LeetCode CH](https://leetcode.cn/problems/count-visited-nodes-in-a-directed-graph/) (Hard)

-   Tags: dynamic programming, graph, memoization
## 2127. Maximum Employees to Be Invited to a Meeting

-   [LeetCode](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/) | [LeetCode CH](https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/) (Hard)

-   Tags: depth first search, graph, topological sort
## 2836. Maximize Value of Function in a Ball Passing Game

-   [LeetCode](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/) | [LeetCode CH](https://leetcode.cn/problems/maximize-value-of-function-in-a-ball-passing-game/) (Hard)

-   Tags: array, dynamic programming, bit manipulation
## 2204. Distance to a Cycle in Undirected Graph

-   [LeetCode](https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/) | [LeetCode CH](https://leetcode.cn/problems/distance-to-a-cycle-in-undirected-graph/) (Hard)

-   Tags: depth first search, breadth first search, union find, graph
