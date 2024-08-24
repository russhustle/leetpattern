from typing import List


def validTree(n: int, edges: List[List[int]]) -> bool:
    if not n:
        return True

    if len(edges) != n - 1:
        return False

    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()

    def dfs(node, parent):
        if node in visit:
            return False

        visit.add(node)

        for child in adj[node]:
            if child == parent:
                continue
            if not dfs(child, node):
                return False

        return True

    return dfs(0, -1) and len(visit) == n


print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # True
print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # False
