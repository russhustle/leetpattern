---
comments: True
---

# Graph BFS

- [x] [994. Rotting Oranges](https://leetcode.cn/problems/rotting-oranges/) (Medium)
- [x] [127. Word Ladder](https://leetcode.cn/problems/word-ladder/) (Hard)
- [x] [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)
- [x] [286. Walls and Gates](https://leetcode.cn/problems/walls-and-gates/) (Medium) 👑
- [x] [815. Bus Routes](https://leetcode.cn/problems/bus-routes/) (Hard)

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

## 127. Word Ladder

-   [LeetCode](https://leetcode.com/problems/word-ladder/) | [LeetCode CH](https://leetcode.cn/problems/word-ladder/) (Hard)

-   Tags: hash table, string, breadth first search
-   The most classic BFS problem.
-   Return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

<iframe width="560" height="315" src="https://www.youtube.com/embed/h9iTnkgv05E?si=51-3ZwweoJrPqRW9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Approach | Time        | Space     |
| -------- | ----------- | --------- |
| BFS      | O(n \* m^2) | O(n \* m) |

```python title="127. Word Ladder - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    n = len(beginWord)
    graph = defaultdict(list)  # pattern: words
    wordList.append(beginWord)

    for word in wordList:
        for i in range(n):
            pattern = word[:i] + "*" + word[i + 1 :]
            graph[pattern].append(word)

    visited = set([beginWord])
    q = deque([beginWord])
    res = 1

    while q:
        size = len(q)
        for _ in range(size):
            word = q.popleft()
            if word == endWord:
                return res

            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1 :]
                for neighbor in graph[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        res += 1

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))  # 5

```

## 1466. Reorder Routes to Make All Paths Lead to the City Zero

-   [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [LeetCode CH](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)

-   Tags: depth first search, breadth first search, graph
-   ![1466](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

```python title="1466. Reorder Routes to Make All Paths Lead to the City Zero - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def minReorderBFS(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))  # go
        graph[v].append((u, 0))  # come

    changes = 0
    q = deque([(0, -1)])

    while q:
        n1, d1 = q.popleft()

        for n2, d2 in graph[n1]:
            if n2 != d1:
                changes += d2
                q.append((n2, n1))

    return changes


# DFS
def minReorderDFS(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))  # go
        graph[v].append((u, 0))  # come

    def dfs(n1, d1):
        changes = 0
        for n2, d2 in graph[n1]:
            if n2 != d1:
                changes += d2 + dfs(n2, n1)
        return changes

    return dfs(0, -1)


n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
print(minReorderBFS(n, connections))  # 2
print(minReorderDFS(n, connections))  # 2

```

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

## 815. Bus Routes

-   [LeetCode](https://leetcode.com/problems/bus-routes/) | [LeetCode CH](https://leetcode.cn/problems/bus-routes/) (Hard)

-   Tags: array, hash table, breadth first search

```python title="815. Bus Routes - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def numBusesToDestination(
    routes: List[List[int]], source: int, target: int
) -> int:
    if source == target:
        return 0

    graph = defaultdict(set)  # {stop: buses}
    for buses, route in enumerate(routes):
        for stop in route:
            graph[stop].add(buses)

    q = deque([(source, 0)])  # (stop, bus)
    visited_stops = set([source])
    visited_buses = set()

    while q:
        stop, bus = q.popleft()

        if stop == target:
            return bus

        for buses in graph[stop]:
            if buses not in visited_buses:
                visited_buses.add(buses)
                for next_stop in routes[buses]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, bus + 1))

    return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
print(numBusesToDestination(routes, source, target))  # 2

```
