"""
-   Determine if a graph can be divided into two groups such that no two nodes of the same group are connected.
"""

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
