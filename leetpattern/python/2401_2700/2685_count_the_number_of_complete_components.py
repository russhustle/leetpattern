from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        v = number of vertices in the component
        e = number of edges in the component
        in complete graph, e = v * (v - 1) / 2
        it counts each edge twice in undirected graph, so e = v * (v - 1)
        """
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = [False for _ in range(n)]

        def dfs(node):
            visited[node] = True
            nonlocal v, e
            v += 1
            e += len(graph[node])
            for adj in graph[node]:
                if not visited[adj]:
                    dfs(adj)

        res = 0
        for i in range(n):
            if not visited[i]:
                v, e = 0, 0
                dfs(i)
                res += e == v * (v - 1)  # check complete component condition

        return res
