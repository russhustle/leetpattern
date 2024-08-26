from typing import List


# Union Find
def countComponents(n: int, edges: List[List[int]]) -> int:
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find(node):
        root = node

        while root != parent[root]:
            parent[root] = parent[parent[root]]
            root = parent[root]
        return root

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1

    count = n
    for n1, n2 in edges:
        count -= union(n1, n2)

    return count


print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))
