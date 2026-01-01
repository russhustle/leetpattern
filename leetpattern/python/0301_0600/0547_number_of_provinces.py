from collections import defaultdict, deque
from typing import List


class FindCircleNum:
    def dfs_adjacency_list(self, isConnected: List[List[int]]) -> int:
        # edge case
        if not isConnected:
            return 0

        # init
        n = len(isConnected)
        visited = set()
        res = 0

        # build adjacency list
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for adj in graph[node]:
                dfs(adj)

        # loop
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res

    def dfs_adjacency_matrix(self, isConnected: List[List[int]]) -> int:
        """
        Time complexity: O(V + E)
        Space complexity: O(V)
        """
        # edge case
        if not isConnected:
            return 0

        # init
        n = len(isConnected)
        visited = set()
        res = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for adj in range(n):
                if node != adj and isConnected[node][adj] == 1:
                    dfs(adj)

        # loop
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res

    def bfs_adjacency_list(self, isConnected: List[List[int]]) -> int:
        # edge case
        if not isConnected:
            return 0

        # init
        n = len(isConnected)
        visited = set()
        res = 0

        # build adjacency list
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        # loop
        for i in range(n):
            if i not in visited:
                q = deque([i])
                visited.add(i)
                res += 1

                while q:
                    node = q.popleft()
                    for adj in graph[node]:
                        if adj not in visited:
                            q.append(adj)
                            visited.add(adj)

        return res

    def bfs_adjacency_matrix(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        res = 0
        visited = set()
        n = len(isConnected)

        for i in range(n):
            if i not in visited:
                q = deque([i])
                visited.add(i)
                res += 1

                while q:
                    cur = q.popleft()
                    for adj in range(n):
                        if (
                            adj != cur
                            and adj not in visited
                            and isConnected[adj][cur] == 1
                        ):
                            q.append(adj)
                            visited.add(adj)

        return res

    def union_find(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}

        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return None

            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        res = len(set(find(i) for i in range(n)))

        return res


if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    sol = FindCircleNum()
    assert sol.dfs_adjacency_list(isConnected) == 2
    assert sol.dfs_adjacency_matrix(isConnected) == 2
    assert sol.bfs_adjacency_list(isConnected) == 2
    assert sol.bfs_adjacency_matrix(isConnected) == 2
    assert sol.union_find(isConnected) == 2
