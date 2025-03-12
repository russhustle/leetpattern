from collections import defaultdict, deque
from typing import List

from template import UnionFind


# DFS (Adjacency Matrix)
def findCircleNumDFSMatrix(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in range(n):
            if node != neighbor and isConnected[node][neighbor] == 1:
                dfs(neighbor)

    res = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            res += 1

    return res


# DFS (Adjacency List)
def findCircleNumDFSList(isConnected: List[List[int]]) -> int:
    graph = defaultdict(list)
    n = len(isConnected)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    res = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            res += 1

    return res


# BFS (Adjacency Matrix)
def findCircleNumBFS(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()
    q = deque()
    res = 0

    for i in range(n):
        if i not in visited:
            res += 1

            q.append(i)
            while q:
                node = q.popleft()
                visited.add(node)
                for node, val in enumerate(isConnected[node]):
                    if val == 1 and node not in visited:
                        q.append(node)
                        visited.add(node)

    return res


# Union Find
def findCircleNumUF(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)

    res = len(set(uf.find(i) for i in range(n)))

    return res


# Union Find
def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    par = {i: i for i in range(n)}
    rank = {i: 0 for i in range(n)}

    def find(n):
        p = par[n]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return None

        if rank[p1] > rank[p2]:
            par[p2] = p1
        elif rank[p1] < rank[p2]:
            par[p1] = p2
        else:
            par[p2] = p1
            rank[p1] += 1

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                union(i, j)

    res = len(set(find(i) for i in range(n)))

    return res


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNumDFSList(isConnected))  # 2
print(findCircleNumDFSMatrix(isConnected))  # 2
print(findCircleNumBFS(isConnected))  # 2
print(findCircleNum(isConnected))  # 2
print(findCircleNumUF(isConnected))  # 2
