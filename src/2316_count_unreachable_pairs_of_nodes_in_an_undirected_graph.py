from collections import defaultdict
from typing import List


# DFS (Adjacency List)
def countPairsList(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node in visited:
            return 0

        visited.add(node)
        count = 1

        for nei in graph[node]:
            if nei not in visited:
                count += dfs(nei)

        return count

    res = 0
    for i in range(n):
        if i not in visited:
            count = dfs(i)
            res += count * (n - count)

    return res // 2


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
print(countPairsList(n, edges))  # 14
