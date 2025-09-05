from collections import deque
from typing import Dict, List
from .graph import compute_degrees_from_adjacency_list


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


# 2. DFS
def topologicalSortDFS(graph: Dict[str, List[str]]) -> List[str]:
    """Topological sort of a directed acyclic graph using DFS

    Args:
        graph (Dict[List]): Adjacency list representation of the graph
        Example:
        {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': []
        }

    Returns:
        List: Topological order of the graph
    """

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(node)

    visited = set()
    order = []
    for node in graph:
        if node not in visited:
            dfs(node)

    return order[::-1]
