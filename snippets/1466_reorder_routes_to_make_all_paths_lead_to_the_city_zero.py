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
