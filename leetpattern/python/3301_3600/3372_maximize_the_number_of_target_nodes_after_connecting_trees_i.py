from typing import Callable, List, Tuple


def maxTargetNodes(edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
    n = len(edges1) + 1
    m = len(edges2) + 1

    def calc_tree(
        edges: List[List[int]], k: int
    ) -> Tuple[int, Callable[[int, int, int], int]]:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        diameter = 0

        def dfs_diameter(x: int, fa: int) -> int:
            nonlocal diameter
            max_len = 0
            for y in g[x]:
                if y != fa:
                    sub_len = dfs_diameter(y, x) + 1
                    diameter = max(diameter, max_len + sub_len)
                    max_len = max(max_len, sub_len)
            return max_len

        dfs_diameter(0, -1)

        def dfs(x: int, fa: int, d: int) -> int:
            if d > k:
                return 0
            cnt = 1
            for y in g[x]:
                if y != fa:
                    cnt += dfs(y, x, d + 1)
            return cnt

        return diameter, dfs

    max2 = 0
    if k:
        diameter, dfs = calc_tree(edges2, k - 1)
        if diameter < k:
            max2 = m  # All nodes in the second tree are target nodes
        else:
            max2 = max(dfs(i, -1, 0) for i in range(m))

    diameter, dfs = calc_tree(edges1, k)
    if diameter <= k:
        return [n + max2] * n  # All nodes in the first tree are target nodes
    return [dfs(i, -1, 0) + max2 for i in range(n)]
