from collections import defaultdict
from typing import List


# Union Find
def numSimilarGroups(strs: List[str]) -> int:
    n = len(strs)
    parent = list(range(n))
    rank = [0 for _ in range(n)]

    def find(n):
        p = parent[n]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return
        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p1] < rank[p2]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            rank[p1] += 1

    def is_similar(s1, s2):
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 2:
                return False
        return True

    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                union(i, j)

    return sum(find(i) == i for i in range(n))


strs = ["tars", "rats", "arts", "star"]
print(numSimilarGroups(strs))  # 2
