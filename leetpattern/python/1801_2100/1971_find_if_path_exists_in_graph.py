from collections import defaultdict
from typing import List


# DFS (Adjacency List)
def validPathDFS(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if not edges and source != destination:
        return False

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(source)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(validPathDFS(n, edges, source, destination))  # True
