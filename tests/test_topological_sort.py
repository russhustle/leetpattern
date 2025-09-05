from leetpattern.utils import khans_algorithm, topological_sort_dfs


def test_khans_algorithm_linear_graph():
    graph = {0: [1], 1: [2], 2: [3], 3: []}
    result = khans_algorithm(graph)
    assert result == [0, 1, 2, 3]


def test_khans_algorithm_dag():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = khans_algorithm(graph)
    assert result in [[0, 1, 2, 3], [0, 2, 1, 3]]


def test_khans_algorithm_cycle():
    graph = {0: [1], 1: [2], 2: [0]}
    result = khans_algorithm(graph)
    assert result == []


def test_khans_algorithm_single_node():
    graph = {0: []}
    result = khans_algorithm(graph)
    assert result == [0]


def test_khans_algorithm_empty_graph():
    graph = {}
    result = khans_algorithm(graph)
    assert result == []


def test_khans_algorithm_complex_dag():
    graph = {0: [1, 3], 1: [2], 2: [4], 3: [2, 4], 4: []}
    result = khans_algorithm(graph)
    assert len(result) == 5
    assert result[0] == 0
    assert result[-1] == 4


def test_topological_sort_dfs_linear_graph():
    graph = {0: [1], 1: [2], 2: [3], 3: []}
    result = topological_sort_dfs(graph)
    assert result == [0, 1, 2, 3]


def test_topological_sort_dfs_dag():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = topological_sort_dfs(graph)
    assert len(result) == 4
    assert result[0] == 0
    assert result[-1] == 3


def test_topological_sort_dfs_single_node():
    graph = {0: []}
    result = topological_sort_dfs(graph)
    assert result == [0]


def test_topological_sort_dfs_empty_graph():
    graph = {}
    result = topological_sort_dfs(graph)
    assert result == []


def test_topological_sort_dfs_complex_dag():
    graph = {0: [1, 3], 1: [2], 2: [4], 3: [2, 4], 4: []}
    result = topological_sort_dfs(graph)
    assert len(result) == 5
    assert result[0] == 0
    assert result[-1] == 4


def test_both_algorithms_same_result():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}
    khan_result = khans_algorithm(graph)
    dfs_result = topological_sort_dfs(graph)

    assert len(khan_result) == len(dfs_result)
    assert set(khan_result) == set(dfs_result)
