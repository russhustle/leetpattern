from collections import defaultdict, deque
from typing import List


# Topological Sort
def eventualSafeNodesTS(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    reverse_graph = defaultdict(list)
    indegree = [0 for _ in range(n)]
    safe = [False for _ in range(n)]

    for u in range(n):
        for v in graph[u]:
            reverse_graph[v].append(u)
        indegree[u] = len(graph[u])

    q = deque([i for i in range(n) if indegree[i] == 0])

    while q:
        node = q.popleft()
        safe[node] = True

        for neighbor in reverse_graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return [i for i in range(n) if safe[i]]


# DFS
def eventualSafeNodesDFS(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    state = [0 for _ in range(n)]  # 0: unvisited, 1: visiting, 2: visited

    def dfs(node):
        if state[node] > 0:
            return state[node] == 2
        state[node] = 1
        for neighbor in graph[node]:
            if state[neighbor] == 1 or not dfs(neighbor):
                return False
        state[node] = 2
        return True

    return [i for i in range(n) if dfs(i)]


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(eventualSafeNodesTS(graph))  # [2, 4, 5, 6]
print(eventualSafeNodesDFS(graph))  # [2, 4, 5, 6]
