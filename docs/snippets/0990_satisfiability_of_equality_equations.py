from collections import defaultdict
from typing import List


# Union Find
def equationsPossible(equations: List[str]) -> bool:
    parent = defaultdict(str)
    rank = defaultdict(int)

    def find(n):
        p = parent[n]
        while p != parent[p]:
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

    for equation in equations:
        if equation[0] not in parent:
            parent[equation[0]] = equation[0]
            rank[equation[0]] = 1
        if equation[3] not in parent:
            parent[equation[3]] = equation[3]
            rank[equation[3]] = 1

    for equation in equations:
        if equation[1] == "=":
            union(equation[0], equation[3])

    for equation in equations:
        if equation[1] == "!":
            if find(equation[0]) == find(equation[3]):
                return False

    return True


equations = ["a==b", "b!=a"]
print(equationsPossible(equations))  # False
