from collections import defaultdict
from typing import List


# Union Find
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    parent = defaultdict(tuple)
    islands = 0
    result = []
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def find(node):
        p = parent[node]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            parent[p1] = p2
            return True
        return False

    for r, c in positions:
        if (r, c) in visited:
            result.append(islands)
            continue

        islands += 1
        parent[(r, c)] = (r, c)
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited:
                if union((r, c), (nr, nc)):
                    islands -= 1

        result.append(islands)

    return result


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(numIslands2(m, n, positions))  # [1, 1, 2, 3]
