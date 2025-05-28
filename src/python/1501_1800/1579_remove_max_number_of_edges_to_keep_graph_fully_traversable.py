"""
- Return the maximum number of edges you can remove so that the graph remains fully traversable.

![1579](../../assets/1579.png){width=200px}
"""

from typing import List


# Kruskal
def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    alice, bob = UnionFind(n), UnionFind(n)
    visited = 0

    for t, u, v in edges:
        if t == 3:
            if alice.union(u, v) | bob.union(u, v):
                visited += 1

    for t, u, v in edges:
        if t == 1:
            if alice.union(u, v):
                visited += 1
        elif t == 2:
            if bob.union(u, v):
                visited += 1

    if alice.components > 1 or bob.components > 1:
        return -1

    return len(edges) - visited


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = {i: 0 for i in range(1, n + 1)}
        self.components = n

    def find(self, n):
        p = self.parent[n]
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        self.components -= 1

        return True


n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
print(maxNumEdgesToRemove(n, edges))  # 2
