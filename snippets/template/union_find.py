class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.par[p] != p:
            self.par[p] = self.find(self.par[p])
        return self.par[p]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.par[p1] = p2
            else:
                self.par[p2] = p1
                self.rank[p1] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


uf = UnionFind(10)
uf.union(1, 2)
uf.union(3, 4)
uf.union(1, 4)
uf.union(5, 6)
print(uf.connected(2, 3))  # True
print(uf.connected(1, 3))  # True
print(uf.connected(1, 5))  # False
