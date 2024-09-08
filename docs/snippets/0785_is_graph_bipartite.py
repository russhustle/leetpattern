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
