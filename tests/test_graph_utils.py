import pytest

from leetpattern.utils.graph_utils import (build_adjacency_list_from_edges,
                                           compute_degrees_from_adjacency_list,
                                           transpose_edges)


def test_compute_degrees_empty_graph():
    graph = {}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {}
    assert out_deg == {}


def test_compute_degrees_single_node_no_edges():
    graph = {0: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0}
    assert out_deg == {0: 0}


def test_compute_degrees_single_edge():
    graph = {0: [1], 1: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0, 1: 1}
    assert out_deg == {0: 1, 1: 0}


def test_compute_degrees_linear_graph():
    graph = {0: [1], 1: [2], 2: [3], 3: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0, 1: 1, 2: 1, 3: 1}
    assert out_deg == {0: 1, 1: 1, 2: 1, 3: 0}


def test_compute_degrees_dag():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0, 1: 1, 2: 1, 3: 2}
    assert out_deg == {0: 2, 1: 1, 2: 1, 3: 0}


def test_compute_degrees_cycle():
    graph = {0: [1], 1: [2], 2: [0]}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 1, 1: 1, 2: 1}
    assert out_deg == {0: 1, 1: 1, 2: 1}


def test_compute_degrees_self_loop():
    graph = {0: [0]}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 1}
    assert out_deg == {0: 1}


def test_compute_degrees_multiple_edges_to_same_node():
    graph = {0: [1, 1, 2], 1: [], 2: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0, 1: 2, 2: 1}
    assert out_deg == {0: 3, 1: 0, 2: 0}


def test_compute_degrees_complex_graph():
    graph = {0: [1, 2, 3], 1: [2, 4], 2: [4], 3: [2, 4], 4: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0, 1: 1, 2: 3, 3: 1, 4: 3}
    assert out_deg == {0: 3, 1: 2, 2: 1, 3: 2, 4: 0}


def test_compute_degrees_disconnected_components():
    graph = {0: [1], 1: [], 2: [3], 3: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert in_deg == {0: 0, 1: 1, 2: 0, 3: 1}
    assert out_deg == {0: 1, 1: 0, 2: 1, 3: 0}


def test_compute_degrees_return_types():
    graph = {0: [1], 1: []}
    in_deg, out_deg = compute_degrees_from_adjacency_list(graph)
    assert isinstance(in_deg, dict)
    assert isinstance(out_deg, dict)
    assert all(
        isinstance(k, int) and isinstance(v, int) for k, v in in_deg.items()
    )
    assert all(
        isinstance(k, int) and isinstance(v, int) for k, v in out_deg.items()
    )


# Tests for transpose_edges
def test_transpose_edges_empty():
    edges = []
    result = transpose_edges(edges)
    assert result == []


def test_transpose_edges_single():
    edges = [[1, 2]]
    result = transpose_edges(edges)
    assert result == [[2, 1]]


def test_transpose_edges_multiple():
    edges = [[1, 2], [2, 3], [3, 4]]
    result = transpose_edges(edges)
    assert result == [[2, 1], [3, 2], [4, 3]]


def test_transpose_edges_self_loop():
    edges = [[1, 1]]
    result = transpose_edges(edges)
    assert result == [[1, 1]]


def test_transpose_edges_bidirectional():
    edges = [[1, 2], [2, 1]]
    result = transpose_edges(edges)
    assert result == [[2, 1], [1, 2]]


# Tests for build_adjacency_list_from_edges
def test_build_adjacency_list_empty_nodes():
    nodes = set()
    edges = []
    result = build_adjacency_list_from_edges(nodes, edges)
    assert result == {}


def test_build_adjacency_list_single_node_no_edges():
    nodes = {0}
    edges = []
    result = build_adjacency_list_from_edges(nodes, edges)
    assert result == {0: []}


def test_build_adjacency_list_directed_simple():
    nodes = {0, 1, 2}
    edges = [[0, 1], [1, 2]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=True)
    assert result == {0: [1], 1: [2], 2: []}


def test_build_adjacency_list_undirected_simple():
    nodes = {0, 1, 2}
    edges = [[0, 1], [1, 2]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=False)
    assert result == {0: [1], 1: [0, 2], 2: [1]}


def test_build_adjacency_list_directed_multiple_edges():
    nodes = {0, 1, 2}
    edges = [[0, 1], [0, 2], [1, 2]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=True)
    assert result == {0: [1, 2], 1: [2], 2: []}


def test_build_adjacency_list_undirected_multiple_edges():
    nodes = {0, 1, 2}
    edges = [[0, 1], [0, 2], [1, 2]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=False)
    assert result == {0: [1, 2], 1: [0, 2], 2: [0, 1]}


def test_build_adjacency_list_self_loop():
    nodes = {0, 1}
    edges = [[0, 0], [0, 1]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=True)
    assert result == {0: [0, 1], 1: []}


def test_build_adjacency_list_undirected_self_loop():
    nodes = {0, 1}
    edges = [[0, 0], [0, 1]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=False)
    assert result == {0: [0, 0, 1], 1: [0]}


def test_build_adjacency_list_duplicate_edges():
    nodes = {0, 1, 2}
    edges = [[0, 1], [0, 1], [1, 2]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=True)
    assert result == {0: [1, 1], 1: [2], 2: []}


def test_build_adjacency_list_complex_graph():
    nodes = {0, 1, 2, 3, 4}
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
    result = build_adjacency_list_from_edges(nodes, edges, directed=True)
    assert result == {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}


def test_build_adjacency_list_return_types():
    nodes = {0, 1}
    edges = [[0, 1]]
    result = build_adjacency_list_from_edges(nodes, edges)
    assert isinstance(result, dict)
    assert all(isinstance(k, int) for k in result.keys())
    assert all(isinstance(v, list) for v in result.values())
    assert all(
        isinstance(neighbor, int)
        for neighbors in result.values()
        for neighbor in neighbors
    )
