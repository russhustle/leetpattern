---
comments: True
---

# Grid BFS

## Table of Contents

- [x] [1926. Nearest Exit from Entrance in Maze](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/) (Medium)
- [x] [1091. Shortest Path in Binary Matrix](https://leetcode.cn/problems/shortest-path-in-binary-matrix/) (Medium)
- [x] [1162. As Far from Land as Possible](https://leetcode.cn/problems/as-far-from-land-as-possible/) (Medium)
- [x] [542. 01 Matrix](https://leetcode.cn/problems/01-matrix/) (Medium)
- [x] [994. Rotting Oranges](https://leetcode.cn/problems/rotting-oranges/) (Medium)
- [x] [1765. Map of Highest Peak](https://leetcode.cn/problems/map-of-highest-peak/) (Medium)
- [x] [934. Shortest Bridge](https://leetcode.cn/problems/shortest-bridge/) (Medium)
- [ ] [2146. K Highest Ranked Items Within a Price Range](https://leetcode.cn/problems/k-highest-ranked-items-within-a-price-range/) (Medium)
- [ ] [1293. Shortest Path in a Grid with Obstacles Elimination](https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/) (Hard)
- [ ] [909. Snakes and Ladders](https://leetcode.cn/problems/snakes-and-ladders/) (Medium)
- [ ] [1210. Minimum Moves to Reach Target with Rotations](https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/) (Hard)
- [ ] [675. Cut Off Trees for Golf Event](https://leetcode.cn/problems/cut-off-trees-for-golf-event/) (Hard)
- [ ] [749. Contain Virus](https://leetcode.cn/problems/contain-virus/) (Hard)
- [ ] [1730. Shortest Path to Get Food](https://leetcode.cn/problems/shortest-path-to-get-food/) (Medium) 👑
- [x] [286. Walls and Gates](https://leetcode.cn/problems/walls-and-gates/) (Medium) 👑
- [x] [490. The Maze](https://leetcode.cn/problems/the-maze/) (Medium) 👑
- [x] [505. The Maze II](https://leetcode.cn/problems/the-maze-ii/) (Medium) 👑
- [x] [499. The Maze III](https://leetcode.cn/problems/the-maze-iii/) (Hard) 👑
- [ ] [317. Shortest Distance from All Buildings](https://leetcode.cn/problems/shortest-distance-from-all-buildings/) (Hard) 👑
- [ ] [2814. Minimum Time Takes to Reach Destination Without Drowning](https://leetcode.cn/problems/minimum-time-takes-to-reach-destination-without-drowning/) (Hard) 👑

## 1926. Nearest Exit from Entrance in Maze

-   [LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) | [LeetCode CH](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/) (Medium)

-   Tags: array, breadth first search, matrix

```python title="1926. Nearest Exit from Entrance in Maze - Python Solution"
from collections import deque
from typing import List


# BFS
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(entrance[0], entrance[1], 0)])
    maze[entrance[0]][entrance[1]] = "+"

    while q:
        r, c, steps = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                if nr in [0, m - 1] or nc in [0, n - 1]:
                    return steps + 1
                q.append((nr, nc, steps + 1))
                maze[nr][nc] = "+"

    return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
print(nearestExit(maze, entrance))  # 1

```

## 1091. Shortest Path in Binary Matrix

-   [LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-in-binary-matrix/) (Medium)

-   Tags: array, breadth first search, matrix

```python title="1091. Shortest Path in Binary Matrix - Python Solution"
from collections import deque
from typing import List


# BFS
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    if n == 1:
        return 1

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    q = deque([(0, 0, 1)])  # (row, column, distance)
    grid[0][0] = 1

    while q:
        r, c, d = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                if nr == nc == n - 1:
                    return d + 1
                q.append((nr, nc, d + 1))
                grid[nr][nc] = 1

    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))  # 4

```

## 1162. As Far from Land as Possible

-   [LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/) | [LeetCode CH](https://leetcode.cn/problems/as-far-from-land-as-possible/) (Medium)

-   Tags: array, dynamic programming, breadth first search, matrix

```python title="1162. As Far from Land as Possible - Python Solution"
from collections import deque
from typing import List


# BFS
def maxDistance(grid: List[List[int]]) -> int:
    n = len(grid)
    res = -1
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    q = deque([[i, j] for i in range(n) for j in range(n) if grid[i][j] == 1])

    if len(q) == (n**2):
        return res

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append([nr, nc])
        res += 1

    return res


grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(maxDistance(grid))  # 4

```

## 542. 01 Matrix

-   [LeetCode](https://leetcode.com/problems/01-matrix/) | [LeetCode CH](https://leetcode.cn/problems/01-matrix/) (Medium)

-   Tags: array, dynamic programming, breadth first search, matrix

```python title="542. 01 Matrix - Python Solution"
from collections import deque
from typing import List


# BFS
def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[float("inf")] * n for _ in range(m)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(mat))
# [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

```

## 994. Rotting Oranges

-   [LeetCode](https://leetcode.com/problems/rotting-oranges/) | [LeetCode CH](https://leetcode.cn/problems/rotting-oranges/) (Medium)

-   Tags: array, breadth first search, matrix
-   Return the minimum number of minutes that must elapse until no cell has a fresh orange.
-   Hint: Multi-source BFS to count the level.

![994](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)


```python title="994. Rotting Oranges - Python Solution"
from collections import deque
from typing import List


# BFS
def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    fresh = 0
    q = deque()
    dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append([i, j])
            elif grid[i][j] == 1:
                fresh += 1
    res = 0

    while q and fresh > 0:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append([nr, nc])
                    grid[nr][nc] = 2
                    fresh -= 1
        res += 1

    return res if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
assert orangesRotting(grid) == 4

```

## 1765. Map of Highest Peak

-   [LeetCode](https://leetcode.com/problems/map-of-highest-peak/) | [LeetCode CH](https://leetcode.cn/problems/map-of-highest-peak/) (Medium)

-   Tags: array, breadth first search, matrix

```python title="1765. Map of Highest Peak - Python Solution"
from collections import deque
from typing import List


# BFS (Multi-Source BFS)
def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    m, n = len(isWater), len(isWater[0])
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    q = deque()

    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                q.append((i, j))
                isWater[i][j] = 0
            else:
                isWater[i][j] = -1

    height = 1
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and isWater[nr][nc] == -1:
                    isWater[nr][nc] = height
                    q.append((nr, nc))
        height += 1

    return isWater


isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(highestPeak(isWater))
# [[1, 1, 0], [0, 1, 1], [1, 2, 2]]

```

## 934. Shortest Bridge

-   [LeetCode](https://leetcode.com/problems/shortest-bridge/) | [LeetCode CH](https://leetcode.cn/problems/shortest-bridge/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix

```python title="934. Shortest Bridge - Python Solution"
from collections import deque
from typing import List


# BFS + DFS; Coloring
def shortestBridge(grid: List[List[int]]) -> int:
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, queue):
        grid[r][c] = 2
        queue.append((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(n) and nc in range(n) and grid[nr][nc] == 1:
                dfs(nr, nc, queue)

    q = deque()
    found = False
    for r in range(n):
        if found:
            break
        for c in range(n):
            if grid[r][c] == 1:
                dfs(r, c, q)
                found = True
                break

    steps = 0
    while q:
        m = len(q)
        for _ in range(m):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n):
                    if grid[nr][nc] == 1:
                        return steps
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        steps += 1

    return -1


grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
print(shortestBridge(grid))  # 1

```

## 2146. K Highest Ranked Items Within a Price Range

-   [LeetCode](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/) | [LeetCode CH](https://leetcode.cn/problems/k-highest-ranked-items-within-a-price-range/) (Medium)

-   Tags: array, breadth first search, sorting, heap priority queue, matrix
## 1293. Shortest Path in a Grid with Obstacles Elimination

-   [LeetCode](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/) (Hard)

-   Tags: array, breadth first search, matrix
## 909. Snakes and Ladders

-   [LeetCode](https://leetcode.com/problems/snakes-and-ladders/) | [LeetCode CH](https://leetcode.cn/problems/snakes-and-ladders/) (Medium)

-   Tags: array, breadth first search, matrix
## 1210. Minimum Moves to Reach Target with Rotations

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/) (Hard)

-   Tags: array, breadth first search, matrix
## 675. Cut Off Trees for Golf Event

-   [LeetCode](https://leetcode.com/problems/cut-off-trees-for-golf-event/) | [LeetCode CH](https://leetcode.cn/problems/cut-off-trees-for-golf-event/) (Hard)

-   Tags: array, breadth first search, heap priority queue, matrix
## 749. Contain Virus

-   [LeetCode](https://leetcode.com/problems/contain-virus/) | [LeetCode CH](https://leetcode.cn/problems/contain-virus/) (Hard)

-   Tags: array, depth first search, breadth first search, matrix, simulation
## 1730. Shortest Path to Get Food

-   [LeetCode](https://leetcode.com/problems/shortest-path-to-get-food/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-to-get-food/) (Medium)

-   Tags: array, breadth first search, matrix
## 286. Walls and Gates

-   [LeetCode](https://leetcode.com/problems/walls-and-gates/) | [LeetCode CH](https://leetcode.cn/problems/walls-and-gates/) (Medium)

-   Tags: array, breadth first search, matrix
![286](https://assets.leetcode.com/uploads/2021/01/03/grid.jpg)


```python title="286. Walls and Gates - Python Solution"
from collections import deque
from typing import List


# Multi-source BFS
def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    m, n = len(rooms), len(rooms[0])
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def addRoom(r, c):
        if (
            r in range(m)
            and c in range(n)
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


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
wallsAndGates(rooms)
print(rooms)
# [[3, -1, 0,  1],
#  [2,  2, 1, -1],
#  [1, -1, 2, -1],
#  [0, -1, 3,  4]]

```

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

## 317. Shortest Distance from All Buildings

-   [LeetCode](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | [LeetCode CH](https://leetcode.cn/problems/shortest-distance-from-all-buildings/) (Hard)

-   Tags: array, breadth first search, matrix
## 2814. Minimum Time Takes to Reach Destination Without Drowning

-   [LeetCode](https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-takes-to-reach-destination-without-drowning/) (Hard)

-   Tags: array, breadth first search, matrix
