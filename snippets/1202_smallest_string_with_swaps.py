from collections import defaultdict
from typing import List


# Union Find
def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    par = list(range(n))
    components = defaultdict(list)

    def find(node):
        p = par[node]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 != p2:
            par[p1] = p2

    for index, j in pairs:
        union(index, j)

    for index in range(n):
        components[find(index)].append(index)

    res = list(s)
    for indices in components.values():
        chars = sorted([s[index] for index in indices])
        for index, char in zip(indices, chars):
            res[index] = char

    return "".join(res)


s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs))  # "bacd"
