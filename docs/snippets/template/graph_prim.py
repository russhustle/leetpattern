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
    heap = []

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


connections = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 0, 4),
]

print(prim(connections))
# {
#     0: [(2, 3)],
#     2: [(0, 3), (1, 1)],
#     1: [(2, 1), (3, 2)],
#     3: [(1, 2), (4, 2)],
#     4: [(3, 2)],
# }
