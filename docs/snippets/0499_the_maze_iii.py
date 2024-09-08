import heapq
from typing import List


# Dijkstra
def findShortestWay(
    maze: List[List[int]], ball: List[int], hole: List[int]
) -> str:
    directions = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]
    m, n = len(maze), len(maze[0])

    dist = [[float("inf")] * n for _ in range(m)]
    dist[ball[0]][ball[1]] = 0

    paths = [[""] * n for _ in range(m)]
    paths[ball[0]][ball[1]] = ""

    heap = [(0, "", ball[0], ball[1])]

    while heap:
        d, path, x, y = heapq.heappop(heap)

        if [x, y] == hole:
            return path

        for dx, dy, direction in directions:
            nx, ny, nd = x, y, d

            while (
                0 <= nx + dx < m
                and 0 <= ny + dy < n
                and maze[nx + dx][ny + dy] == 0
            ):
                nx += dx
                ny += dy
                nd += 1

                if [nx, ny] == hole:
                    break

            new_path = path + direction
            if nd < dist[nx][ny] or (
                nd == dist[nx][ny] and new_path < paths[nx][ny]
            ):
                dist[nx][ny] = nd
                paths[nx][ny] = new_path
                heapq.heappush(heap, (nd, new_path, nx, ny))

    return "impossible"


maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
]
ball = [4, 3]
hole = [0, 1]
print(findShortestWay(maze, ball, hole))  # "lul"
