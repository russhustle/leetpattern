from collections import defaultdict
from typing import List


# DFS
def minScoreDFS(n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    res = float("inf")
    visited = set([1])

    def dfs(node):
        nonlocal res
        for nxt, dist in graph[node]:
            res = min(res, dist)
            if nxt not in visited:
                visited.add(nxt)
                dfs(nxt)

    dfs(1)

    return res


n = 4
roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
print(minScoreDFS(n, roads))  # 5
