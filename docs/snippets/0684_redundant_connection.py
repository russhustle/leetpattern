from typing import List


# Union Find
def findRedundantConnectionUF(edges: List[List[int]]) -> List[int]:
    par = {i: i for i in range(len(edges) + 1)}
    rank = {i: 1 for i in range(len(edges) + 1)}

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]

        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return (n1, n2)


# DFS
def findRedundantConnectionDFS(edges: List[List[int]]) -> List[int]:
    graph, cycle = {}, {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    def dfs(node, parent):
        if node in cycle:
            for k in list(cycle.keys()):
                if k == node:
                    return True
                del cycle[k]

        cycle[node] = None
        for child in graph[node]:
            if child != parent and dfs(child, node):
                return True
        del cycle[node]
        return False

    dfs(edges[0][0], -1)
    for a, b in edges[::-1]:
        if a in cycle and b in cycle:
            return (a, b)


edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantConnectionUF(edges))  # (2, 3)
print(findRedundantConnectionDFS(edges))  # (2, 3)
