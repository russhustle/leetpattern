import heapq
from collections import defaultdict
from typing import Dict, List, Tuple


def prim(
    graph: Dict[str, List[Tuple[str, int]]]
) -> Dict[str, List[Tuple[str, int]]]:
    mst = defaultdict(list)
    visited = set()

    min_heap = []
    start = next(iter(graph))  # get the first node
    visited.add(start)

    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue

        visited.add(v)
        mst[u].append((v, weight))

        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, v, neighbor))

    return mst


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

print(prim(graph))
# {'A': [('B', 1)], 'B': [('C', 2)], 'C': [('D', 1)]})
