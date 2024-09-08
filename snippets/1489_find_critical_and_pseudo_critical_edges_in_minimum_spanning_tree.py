from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.part = n

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
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

        self.part -= 1
        return True


# Kruskal
def findCriticalAndPseudoCriticalEdges(
    n: int, edges: List[List[int]]
) -> List[List[int]]:
    m = len(edges)

    # Add index to edges
    lst = list(range(m))
    lst.sort(key=lambda x: edges[x][2])

    # Calculate minimum cost
    min_cost = 0
    uf = UnionFind(n)
    for i in lst:
        x, y, cost = edges[i]
        if uf.union(x, y):
            min_cost += cost

    # Calculate key edges
    key = set()
    for i in lst:
        cur_cost = 0
        uf = UnionFind(n)
        for j in lst:
            if j != i:
                x, y, cost = edges[j]
                if uf.union(x, y):
                    cur_cost += cost
        if cur_cost > min_cost or uf.part != 1:
            key.add(i)

    # Calculate fake edges
    fake = set()
    for i in lst:
        if i not in key:
            cur_cost = edges[i][2]
            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            for j in lst:
                x, y, cost = edges[j]
                if uf.union(x, y):
                    cur_cost += cost
            if cur_cost == min_cost and uf.part == 1:
                fake.add(i)

    return [sorted(list(key)), sorted(list(fake))]


n = 5
edges = [
    [0, 1, 1],
    [1, 2, 1],
    [2, 3, 2],
    [0, 3, 2],
    [0, 4, 3],
    [3, 4, 3],
    [1, 4, 6],
]
print(findCriticalAndPseudoCriticalEdges(n, edges))
