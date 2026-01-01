from collections import defaultdict
from typing import List


class remainingMethods:
    def DFS(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i, j in invocations:
            graph[i].append(j)

        sus = set()

        def dfs(node):
            sus.add(node)
            for adj in graph[node]:
                if adj not in sus:
                    dfs(adj)

        dfs(k)

        for i, j in invocations:
            if i not in sus and j in sus:
                return list(range(n))

        return list(set(range(n)) - sus)
