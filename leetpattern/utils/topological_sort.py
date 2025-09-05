from collections import deque
from typing import Dict, List

from leetpattern.utils import compute_degrees_from_adjacency_list


def khans_algorithm(graph: Dict[int, List[int]]) -> List[int]:
    indegree, _ = compute_degrees_from_adjacency_list(graph)

    q = deque([node for node in graph if indegree[node] == 0])
    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if len(order) == len(graph):
        return order
    else:
        return []


def topological_sort_dfs(graph: Dict[int, List[int]]) -> List[int]:
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order[::-1]
