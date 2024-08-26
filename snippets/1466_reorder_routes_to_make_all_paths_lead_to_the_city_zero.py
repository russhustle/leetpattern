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
        node, parent = q.popleft()

        for child, direction in graph[node]:
            if child != parent:
                changes += direction
                q.append((child, node))

    return changes


# DFS
def minReorderDFS(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))  # go
        graph[v].append((u, 0))  # come

    def dfs(node, parent):
        changes = 0
        for child, direction in graph[node]:
            if child != parent:
                changes += direction + dfs(child, node)
        return changes

    return dfs(0, -1)


n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
print(minReorderBFS(n, connections))  # 2
print(minReorderDFS(n, connections))  # 2
