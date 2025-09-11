import heapq
from typing import List


# Dijkstra's
def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
    graph = {i: {} for i in range(n)}
    for u, v, cnt in edges:
        graph[u][v] = cnt
        graph[v][u] = cnt

    heap = [(-maxMoves, 0)]
    seen = {}

    while heap:
        moves, node = heapq.heappop(heap)
        if node in seen:
            continue
        seen[node] = -moves
        for nxt, cnt in graph[node].items():
            movesLeft = -moves - cnt - 1
            if nxt not in seen and movesLeft >= 0:
                heapq.heappush(heap, (-movesLeft, nxt))

    res = len(seen)
    for u, v, cnt in edges:
        res += min(seen.get(u, 0) + seen.get(v, 0), cnt)

    return res


edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
maxMoves = 6
n = 3
print(reachableNodes(None, edges, maxMoves, n))  # 13
