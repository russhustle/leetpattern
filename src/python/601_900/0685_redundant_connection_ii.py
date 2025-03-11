from typing import List


# Union Find
def findRedundantDirectedConnectionUF(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n + 1)
    parent = list(range(n + 1))
    candidates = []

    for u, v in edges:
        if parent[v] != v:
            candidates.append([parent[v], v])
            candidates.append([u, v])
        else:
            parent[v] = u

    if not candidates:
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]

    for u, v in edges:
        if [u, v] == candidates[1]:
            continue
        if not uf.union(u, v):
            return candidates[0]

    return candidates[1]


class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        self.par[p1] = p2
        return True


edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantDirectedConnectionUF(edges))
