from collections import defaultdict
from typing import List


# Graph
def validTree(n: int, edges: List[List[int]]) -> bool:
    if n == 0:
        return False
    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent and not dfs(neighbor, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n


print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # True
print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # False
