import heapq
from collections import defaultdict
from typing import Dict, List, Tuple


def prim(
    connections: List[Tuple[int, int, int]]
) -> Dict[int, List[Tuple[int, int]]]:
    graph = defaultdict(list)
    for u, v, w in connections:
        graph[u].append((v, w))
        graph[v].append((u, w))

    mst = defaultdict(list)  # {node: [(neighbour, weight)]}
    visited = set()
    start = next(iter(graph))
    visited.add(start)
    heap = []  # [(weight, src, dst)]

    for n, w in graph[start]:
        heapq.heappush(heap, (w, start, n))

    while heap:
        w, u, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)
        mst[u].append((v, w))
        mst[v].append((u, w))

        for n, w in graph[v]:
            heapq.heappush(heap, (w, v, n))

    return mst


# Kruskal
def kruskal(
    num: int, connections: List[Tuple[int, int, int]]
) -> Dict[int, List[Tuple[int, int]]]:

    par = {i: i for i in range(num)}
    rank = {i: 0 for i in range(num)}

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
        elif rank[p1] < rank[p2]:
            par[p1] = p2
        else:
            par[p2] = p1
            rank[p1] += 1

        return True

    mst = defaultdict(list)
    heap = []
    for u, v, w in connections:
        heapq.heappush(heap, (w, u, v))

    while heap:
        w, u, v = heapq.heappop(heap)

        if union(u, v):
            mst[u].append((v, w))
            mst[v].append((u, w))

    return mst


connections = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 0, 4),
]
num = 5

print(prim(connections))
# {
#     0: [(2, 3)],
#     2: [(0, 3), (1, 1)],
#     1: [(2, 1), (3, 2)],
#     3: [(1, 2), (4, 2)],
#     4: [(3, 2)],
# }
print(kruskal(num, connections))
# {
#     1: [(2, 1), (3, 2)],
#     2: [(1, 1), (0, 3)],
#     3: [(1, 2), (4, 2)],
#     4: [(3, 2)],
#     0: [(2, 3)]
# }
