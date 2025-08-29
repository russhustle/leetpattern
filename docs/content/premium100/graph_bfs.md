---
comments: True
---

# Graph BFS

## Table of Contents

- [x] [490. The Maze](https://leetcode.cn/problems/the-maze/) (Medium) 👑
- [x] [505. The Maze II](https://leetcode.cn/problems/the-maze-ii/) (Medium) 👑
- [x] [499. The Maze III](https://leetcode.cn/problems/the-maze-iii/) (Hard) 👑
- [ ] [1197. Minimum Knight Moves](https://leetcode.cn/problems/minimum-knight-moves/) (Medium) 👑
- [x] [286. Walls and Gates](https://leetcode.cn/problems/walls-and-gates/) (Medium) 👑
- [ ] [317. Shortest Distance from All Buildings](https://leetcode.cn/problems/shortest-distance-from-all-buildings/) (Hard) 👑
- [x] [269. Alien Dictionary](https://leetcode.cn/problems/alien-dictionary/) (Hard) 👑

## 490. The Maze

-   [LeetCode](https://leetcode.com/problems/the-maze/) | [LeetCode CH](https://leetcode.cn/problems/the-maze/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix
```python title="490. The Maze - Python Solution"
from collections import deque
from typing import List


# BFS
def hasPathBFS(
    maze: List[List[int]], start: List[int], destination: List[int]
) -> bool:
    m, n = len(maze), len(maze[0])
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque([start])
    maze[start[0]][start[1]] = -1

    while q:
        r, c = q.popleft()
        if [r, c] == destination:
            return True

        for dr, dc in dirs:
            nr, nc = r, c

            while (
                0 <= nr + dr < m
                and 0 <= nc + dc < n
                and maze[nr + dr][nc + dc] != 1
            ):
                nr += dr
                nc += dc

            if maze[nr][nc] != -1:
                q.append([nr, nc])
                maze[nr][nc] = -1

    return False


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start = [0, 4]
destination = [4, 4]
print(hasPathBFS(maze, start, destination))  # True

```

## 505. The Maze II

-   [LeetCode](https://leetcode.com/problems/the-maze-ii/) | [LeetCode CH](https://leetcode.cn/problems/the-maze-ii/) (Medium)

-   Tags: array, depth first search, breadth first search, graph, heap priority queue, matrix, shortest path
```python title="505. The Maze II - Python Solution"
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

```

## 499. The Maze III

-   [LeetCode](https://leetcode.com/problems/the-maze-iii/) | [LeetCode CH](https://leetcode.cn/problems/the-maze-iii/) (Hard)

-   Tags: array, string, depth first search, breadth first search, graph, heap priority queue, matrix, shortest path
```python title="499. The Maze III - Python Solution"
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

```

## 1197. Minimum Knight Moves

-   [LeetCode](https://leetcode.com/problems/minimum-knight-moves/) | [LeetCode CH](https://leetcode.cn/problems/minimum-knight-moves/) (Medium)

-   Tags: breadth first search
## 286. Walls and Gates

-   [LeetCode](https://leetcode.com/problems/walls-and-gates/) | [LeetCode CH](https://leetcode.cn/problems/walls-and-gates/) (Medium)

-   Tags: array, breadth first search, matrix
```python title="286. Walls and Gates - Python Solution"
from collections import deque
from typing import List


# Multi-Source BFS
def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    m, n = len(rooms), len(rooms[0])
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def addRoom(r, c):
        if (
            0 <= r < m
            and 0 <= c < n
            and (r, c) not in visited
            and rooms[r][c] != -1
        ):
            q.append((r, c))
            visited.add((r, c))

    q = deque()
    for r in range(m):
        for c in range(n):
            if rooms[r][c] == 0:
                q.append((r, c))
                visited.add((r, c))

    dist = 0

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = dist

            for dr, dc in directions:
                addRoom(r + dr, c + dc)
        dist += 1


if __name__ == "__main__":
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    wallsAndGates(rooms)
    assert rooms == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

```

## 317. Shortest Distance from All Buildings

-   [LeetCode](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | [LeetCode CH](https://leetcode.cn/problems/shortest-distance-from-all-buildings/) (Hard)

-   Tags: array, breadth first search, matrix
## 269. Alien Dictionary

-   [LeetCode](https://leetcode.com/problems/alien-dictionary/) | [LeetCode CH](https://leetcode.cn/problems/alien-dictionary/) (Hard)

-   Tags: array, string, depth first search, breadth first search, graph, topological sort
-   Return the correct order of characters in the alien language.

```python title="269. Alien Dictionary - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS - Kahn's algorithm (Topological Sort)
def alienOrderBFS(words: List[str]) -> str:
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        for j in range(minLen):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    q = deque([c for c in indegree if indegree[c] == 0])
    result = []

    while q:
        char = q.popleft()
        result.append(char)

        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return "".join(result) if len(result) == len(indegree) else ""


# DFS - Topological Sort
def alienOrderDFS(words: List[str]) -> str:
    graph = defaultdict(set)
    visited = {}
    result = []

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        for j in range(minLen):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                break

    def dfs(c):
        if c in visited:
            return visited[c]

        visited[c] = False
        for neighbor in graph[c]:
            if not dfs(neighbor):
                return False

        visited[c] = True
        result.append(c)
        return True

    for c in list(graph.keys()):
        if not dfs(c):
            return ""

    return "".join(result[::-1])


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrderBFS(words))  # wertf
print(alienOrderDFS(words))  # wertf

```
