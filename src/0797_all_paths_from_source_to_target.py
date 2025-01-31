from collections import deque
from typing import List


# DFS - Backtracking
def allPathsSourceTargetDFS(graph: List[List[int]]) -> List[List[int]]:
    result = []
    n = len(graph)

    def dfs(node, path):
        if node == n - 1:
            result.append(path.copy())
            return None

        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            path.pop()

    dfs(0, [0])

    return result


# BFS
def allPathsSourceTargetBFS(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    result = []
    q = deque([(0, [0])])

    while q:
        node, path = q.popleft()

        if node == n - 1:
            result.append(path)

        for nei in graph[node]:
            q.append((nei, path + [nei]))

    return result


graph = [[1, 2], [3], [3], []]
print(allPathsSourceTargetDFS(graph))  # [[0, 1, 3], [0, 2, 3]]
print(allPathsSourceTargetBFS(graph))  # [[0, 1, 3], [0, 2, 3]]
