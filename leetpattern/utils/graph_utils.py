from typing import Dict, List, Tuple


def compute_degrees_from_adjacency_list(
    graph: Dict[int, List[int]],
) -> Tuple[Dict[int, int], Dict[int, int]]:
    """Compute in-degrees and out-degrees of each node in a directed graph"""
    in_deg = {node: 0 for node in graph}
    out_deg = {node: len(graph[node]) for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_deg[neighbor] += 1
    return in_deg, out_deg


def transpose_edges(edges: list[list[int]]) -> list[list[int]]:
    """Transpose (reverse) all edges in the given edge list."""
    return [[v, u] for u, v in edges]


def build_adjacency_list_from_edges(
    nodes: set[int], edges: list[list[int]], directed: bool = True
) -> dict[int, list[int]]:
    """Builds a graph from the given nodes and edges."""
    if not nodes:
        return {}
    graph = {node: [] for node in nodes}
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph
