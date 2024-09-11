class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, n):
        p = self.parent[n]
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


uf = UnionFind(7)
uf.union(1, 2)
uf.union(3, 4)
uf.union(1, 4)
uf.union(5, 6)
print(uf.connected(2, 3))  # True
print(uf.connected(1, 3))  # True
print(uf.connected(1, 5))  # False
