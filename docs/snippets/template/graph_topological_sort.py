from collections import defaultdict, deque
from typing import Dict, List


# 1. BFS - Khan's algorithm
def topologicalSortBFS(graph: Dict[str, List[str]]) -> List[str]:
    """Topological sort of a directed acyclic graph using BFS

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
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

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


graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

print(topologicalSortBFS(graph))  # ['A', 'B', 'C', 'D']
print(topologicalSortDFS(graph))  # ['A', 'C', 'B', 'D']
