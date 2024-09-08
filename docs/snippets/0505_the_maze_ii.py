import heapq
from typing import List


# Dijkstra
def shortestDistance(
    maze: List[List[int]], start: List[int], destination: List[int]
) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n = len(maze), len(maze[0])

    dist = [[float("inf")] * n for _ in range(m)]
    dist[start[0]][start[1]] = 0

    heap = [(0, start[0], start[1])]

    while heap:
        d, r, c = heapq.heappop(heap)

        if [r, c] == destination:
            return d

        for dr, dc in directions:
            nr, nc, nd = r, c, d

            while (
                0 <= nr + dr < m
                and 0 <= nc + dc < n
                and maze[nr + dr][nc + dc] == 0
            ):
                nr += dr
                nc += dc
                nd += 1

            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                heapq.heappush(heap, (nd, nr, nc))

    return -1


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start = [0, 4]
destination = [4, 4]
print(shortestDistance(maze, start, destination))  # 12
