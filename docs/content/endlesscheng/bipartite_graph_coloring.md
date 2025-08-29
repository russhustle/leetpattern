---
comments: True
---

# Bipartite Graph Coloring

## Table of Contents

- [x] [785. Is Graph Bipartite?](https://leetcode.cn/problems/is-graph-bipartite/) (Medium)
- [x] [886. Possible Bipartition](https://leetcode.cn/problems/possible-bipartition/) (Medium)

## 785. Is Graph Bipartite?

-   [LeetCode](https://leetcode.com/problems/is-graph-bipartite/) | [LeetCode CH](https://leetcode.cn/problems/is-graph-bipartite/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
-   Determine if a graph is bipartite.

How to group

|          | Uncolored | Color 1 | Color 2 | Operation   |
| -------- | --------- | ------- | ------- | ----------- |
| Method 1 | -1        | 0       | 1       | `1 - color` |
| Method 2 | 0         | 1       | -1      | `-color`    |

```python title="785. Is Graph Bipartite? - Python Solution"
from collections import deque
from typing import List


# BFS
def isBipartiteBFS(graph: List[List[int]]) -> bool:
    n = len(graph)
    # -1: not colored; 0: blue; 1: red
    color = [-1 for _ in range(n)]

    def bfs(node):
        q = deque([node])
        color[node] = 0

        while q:
            cur = q.popleft()

            for neighbor in graph[cur]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[cur]
                    q.append(neighbor)
                elif color[neighbor] == color[cur]:
                    return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                return False

    return True


# DFS
def isBipartiteDFS(graph: List[List[int]]) -> bool:
    n = len(graph)
    # -1: not colored; 0: blue; 1: red
    color = [-1] * n

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False

    return True


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |    BFS     | O(V+E) |  O(V)   |
# |    DFS     | O(V+E) |  O(V)   |
# |------------|--------|---------|


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(isBipartiteBFS(graph))  # False
print(isBipartiteDFS(graph))  # False

```

## 886. Possible Bipartition

-   [LeetCode](https://leetcode.com/problems/possible-bipartition/) | [LeetCode CH](https://leetcode.cn/problems/possible-bipartition/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
-   Determine if a graph can be divided into two groups such that no two nodes of the same group are connected.

```python title="886. Possible Bipartition - Python Solution"
from collections import deque
from typing import List


# BFS
def possibleBipartitionBFS(n: int, dislikes: List[List[int]]) -> bool:
    group = {i: -1 for i in range(1, n + 1)}

    # Undirected graph
    graph = {i: [] for i in range(1, n + 1)}
    for i, j in dislikes:
        graph[i].append(j)
        graph[j].append(i)

    def bfs(person):
        q = deque([person])
        group[person] = 0

        while q:
            cur = q.popleft()

            for neighbor in graph[cur]:
                if group[neighbor] == -1:
                    group[neighbor] = 1 - group[cur]
                    q.append(neighbor)
                elif group[neighbor] == group[cur]:
                    return False
        return True

    for i in range(1, n + 1):
        if group[i] == -1:
            if not bfs(i):
                return False
    return True


# DFS
def possibleBipartitionDFS(n: int, dislikes: List[List[int]]) -> bool:
    group = {i: -1 for i in range(1, n + 1)}
    graph = {i: [] for i in range(1, n + 1)}
    for i, j in dislikes:
        graph[i].append(j)
        graph[j].append(i)

    def dfs(person, g):
        group[person] = g

        for neighbor in graph[person]:
            if group[neighbor] == -1:
                if not dfs(neighbor, 1 - g):
                    return False
            elif group[neighbor] == g:
                return False

        return True

    for i in range(1, n + 1):
        if group[i] == -1:
            if not dfs(i, 0):
                return False

    return True


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |    BFS     | O(V+E) |  O(V+E) |
# |    DFS     | O(V+E) |  O(V+E) |
# |------------|--------|---------|


n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
print(possibleBipartitionBFS(n, dislikes))  # True
print(possibleBipartitionDFS(n, dislikes))  # True

```
