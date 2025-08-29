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
