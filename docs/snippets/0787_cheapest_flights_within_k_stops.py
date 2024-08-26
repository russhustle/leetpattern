from collections import defaultdict, deque
from typing import List


# Bellman-Ford
def findCheapestPriceBF(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    dist = [float("inf")] * n
    dist[src] = 0

    for _ in range(k + 1):
        temp = dist[:]
        for u, v, w in flights:
            temp[v] = min(temp[v], dist[u] + w)
        dist = temp

    return dist[dst] if dist[dst] != float("inf") else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPriceBF(n, flights, src, dst, k))  # 700
