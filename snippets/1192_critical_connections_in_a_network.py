from collections import defaultdict
from typing import List


# Tarjan
def criticalConnections(
    n: int, connections: List[List[int]]
) -> List[List[int]]:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    bridges = []
    time = 0

    def dfs(n1, prev):
        nonlocal time
        disc[n1], low[n1] = time, time
        time += 1

        for n2 in graph[n1]:
            if n2 == prev:
                continue
            if disc[n2] == -1:
                dfs(n2, n1)
                low[n1] = min(low[n1], low[n2])

                if low[n2] > disc[n1]:
                    bridges.append([n1, n2])
            else:
                low[n1] = min(low[n1], disc[n2])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return bridges


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(criticalConnections(n, connections))  # [[1, 3]]
