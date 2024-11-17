from typing import List

from template import UnionFind


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

    connected_components = len(set(find(i) for i in range(n)))

    return connected_components


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))  # 2
print(findCircleNumUF(isConnected))  # 2
