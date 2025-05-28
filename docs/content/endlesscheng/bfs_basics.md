---
comments: True
---

# BFS Basics

## Table of Contents

- [x] [3243. Shortest Distance After Road Addition Queries I](https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/) (Medium)
- [ ] [1311. Get Watched Videos by Your Friends](https://leetcode.cn/problems/get-watched-videos-by-your-friends/) (Medium)
- [x] [1129. Shortest Path with Alternating Colors](https://leetcode.cn/problems/shortest-path-with-alternating-colors/) (Medium)
- [ ] [1298. Maximum Candies You Can Get from Boxes](https://leetcode.cn/problems/maximum-candies-you-can-get-from-boxes/) (Hard)
- [ ] [2039. The Time When the Network Becomes Idle](https://leetcode.cn/problems/the-time-when-the-network-becomes-idle/) (Medium)
- [ ] [2608. Shortest Cycle in a Graph](https://leetcode.cn/problems/shortest-cycle-in-a-graph/) (Hard)
- [x] [815. Bus Routes](https://leetcode.cn/problems/bus-routes/) (Hard)

## 3243. Shortest Distance After Road Addition Queries I

-   [LeetCode](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/) | [LeetCode CH](https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/) (Medium)

-   Tags: array, breadth first search, graph
- `n=5`, `queries = [[2,4],[0,2],[0,4]]`
- ![1](https://assets.leetcode.com/uploads/2024/06/28/image8.jpg)
- ![2](https://assets.leetcode.com/uploads/2024/06/28/image9.jpg)
- ![3](https://assets.leetcode.com/uploads/2024/06/28/image10.jpg)
- Output: `[3,2,1]`


```python title="3243. Shortest Distance After Road Addition Queries I - Python Solution"
from collections import deque
from itertools import count
from typing import List


# BFS
def shortestDistanceAfterQueries(
    n: int, queries: List[List[int]]
) -> List[int]:
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[i].append(i + 1)

    vis = [-1 for _ in range(n)]

    def bfs(i: int) -> int:
        q = deque([0])
        for step in count(1):
            tmp = q
            q = deque()
            for x in tmp:
                for y in g[x]:
                    if y == n - 1:
                        return step
                    if vis[y] != i:
                        vis[y] = i
                        q.append(y)
        return -1

    res = [0] * len(queries)
    for i, (l, r) in enumerate(queries):
        g[l].append(r)
        res[i] = bfs(i)

    return res


n = 5
queries = [[2, 4], [0, 2], [0, 4]]
print(shortestDistanceAfterQueries(n, queries))  # [3, 2, 1]

```

## 1311. Get Watched Videos by Your Friends

-   [LeetCode](https://leetcode.com/problems/get-watched-videos-by-your-friends/) | [LeetCode CH](https://leetcode.cn/problems/get-watched-videos-by-your-friends/) (Medium)

-   Tags: array, hash table, breadth first search, graph, sorting
## 1129. Shortest Path with Alternating Colors

-   [LeetCode](https://leetcode.com/problems/shortest-path-with-alternating-colors/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-with-alternating-colors/) (Medium)

-   Tags: breadth first search, graph

```python title="1129. Shortest Path with Alternating Colors - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def shortestAlternatingPaths(
    n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
) -> List[int]:
    red_graph = defaultdict(list)
    blue_graph = defaultdict(list)

    for u, v in redEdges:
        red_graph[u].append(v)
    for u, v in blueEdges:
        blue_graph[u].append(v)

    answer = [-1 for _ in range(n)]
    q = deque([(0, 0, 0), (0, 0, 1)])  # (node, distance, color)
    visited = set()

    while q:
        node, dist, color = q.popleft()
        if (node, color) in visited:
            continue
        visited.add((node, color))
        if answer[node] == -1:
            answer[node] = dist
        if color == 0:
            for neighbor in blue_graph[node]:
                q.append((neighbor, dist + 1, 1))
        else:
            for neighbor in red_graph[node]:
                q.append((neighbor, dist + 1, 0))

    return answer


n = 3
red_edges = [[0, 1], [1, 2]]
blue_edges = []
print(shortestAlternatingPaths(n, red_edges, blue_edges))  # [0, 1, -1]

```

## 1298. Maximum Candies You Can Get from Boxes

-   [LeetCode](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/) | [LeetCode CH](https://leetcode.cn/problems/maximum-candies-you-can-get-from-boxes/) (Hard)

-   Tags: array, breadth first search, graph
## 2039. The Time When the Network Becomes Idle

-   [LeetCode](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/) | [LeetCode CH](https://leetcode.cn/problems/the-time-when-the-network-becomes-idle/) (Medium)

-   Tags: array, breadth first search, graph
## 2608. Shortest Cycle in a Graph

-   [LeetCode](https://leetcode.com/problems/shortest-cycle-in-a-graph/) | [LeetCode CH](https://leetcode.cn/problems/shortest-cycle-in-a-graph/) (Hard)

-   Tags: breadth first search, graph
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
