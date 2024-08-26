from collections import defaultdict, deque
from typing import List


# 1. BFS - Kahn's Algorithm
def canFinishBFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = defaultdict(list)
    indegree = [0] * numCourses

    for crs, pre in prerequisites:
        adj[pre].append(crs)
        indegree[crs] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0

    while q:
        crs = q.popleft()
        count += 1

        for next in adj[crs]:
            indegree[next] -= 1

            if indegree[next] == 0:
                q.append(next)

    return count == numCourses


# 2. DFS + Set
def canFinishDFS1(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = defaultdict(list)
    for crs, pre in prerequisites:
        adj[crs].append(pre)

    visited = set()

    def dfs(crs):
        if crs in visited:  # cycle detected
            return False
        if adj[crs] == []:
            return True

        visited.add(crs)

        for pre in adj[crs]:
            if not dfs(pre):
                return False

        visited.remove(crs)
        adj[crs] = []

        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


# 3. DFS + List
def canFinishDFS2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = defaultdict(list)
    for pre, crs in prerequisites:
        adj[crs].append(pre)

    # 0: not visited, 1: visiting, 2: visited
    visited = [0] * numCourses

    def dfs(crs):
        if visited[crs] == 1:  # cycle detected
            return False
        if visited[crs] == 2:
            return True

        visited[crs] = 1

        for pre in adj[crs]:
            if not dfs(pre):
                return False

        visited[crs] = 2
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(canFinishBFS(5, prerequisites))  # True
print(canFinishDFS1(5, prerequisites))  # True
print(canFinishDFS2(5, prerequisites))  # True
