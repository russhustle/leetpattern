from collections import defaultdict
from typing import List


# DFS (Adjacency List)
def countPairsList1(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        visited.add(node)
        size = 1

        for nei in graph[node]:
            if nei not in visited:
                size += dfs(nei)

        return size

    res = 0
    for i in range(n):
        if i not in visited:
            size = dfs(i)
            res += size * (n - size)

    return res // 2


# DFS(Adjacency List)
def countPairsList2(n: int, edges: List[List[int]]) -> int:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False for _ in range(n)]

    def dfs(node):
        visited[node] = True
        size = 1
        for nei in graph[node]:
            if not visited[nei]:
                size += dfs(nei)
        return size

    res, total = 0, 0
    for i in range(n):
        if not visited[i]:
            size = dfs(i)
            res += size * total
            total += size

    return res


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
print(countPairsList1(n, edges))  # 14
print(countPairsList2(n, edges))  # 14
