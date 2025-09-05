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
