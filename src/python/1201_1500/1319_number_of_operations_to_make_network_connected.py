"""
- Return the minimum number of operations needed to make all computers connected.

![1319](https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png)
"""

"""
Edge case: If the number of connections is less than n - 1, it is impossible to connect all the computers.
"""

from collections import defaultdict, deque
from typing import List


# DFS
def makeConnectedDFS(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    component_count = 0

    def dfs(node):
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                dfs(i)

    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            component_count += 1

    return component_count - 1


# BFS
def makeConnectedBFS(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    visited = set()
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(node):
        q = deque([node])
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)

    component_count = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            bfs(i)
            component_count += 1

    return component_count - 1


n = 4
connections = [[0, 1], [0, 2], [1, 2]]
print(makeConnectedDFS(n, connections))  # 1
print(makeConnectedBFS(n, connections))  # 1
