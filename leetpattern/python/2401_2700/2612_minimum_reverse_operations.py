from collections import deque
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, n: int) -> int:
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1: int, n2: int) -> None:
        self.parent[self.find(n1)] = self.find(n2)


def minReverseOperations(n: int, p: int, banned: List[int], k: int) -> List[int]:
    indices = UnionFind(n + 2)
    indices.union(p, p + 2)

    for i in banned:
        indices.union(i, i + 2)

    res = [-1] * n
    res[p] = 0
    q = deque([p])

    while q:
        i = q.popleft()
        mn = max(i - k + 1, k - i - 1)
        mx = min(i + k - 1, n * 2 - k - i - 1)
        j = indices.find(mn)
        while j <= mx:
            res[j] = res[i] + 1
            q.append(j)
            indices.union(j, mx + 2)
            j = indices.find(j + 2)

    return res


if __name__ == "__main__":
    n = 4
    p = 0
    banned = [1, 2]
    k = 4
    print(minReverseOperations(n, p, banned, k))
    # [0, -1, -1, 1]
