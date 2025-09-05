import pytest
from leetpattern.utils import compute_degrees_from_adjacency_list


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
    graph = {
        0: [1, 2, 3],
        1: [2, 4],
        2: [4],
        3: [2, 4],
        4: []
    }
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
    assert all(isinstance(k, int) and isinstance(v, int) for k, v in in_deg.items())
    assert all(isinstance(k, int) and isinstance(v, int) for k, v in out_deg.items())