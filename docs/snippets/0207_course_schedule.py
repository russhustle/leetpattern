from collections import deque
from typing import List


# BFS
def canFinishBFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    in_degree = [0 for _ in range(numCourses)]
    graph = [[] for _ in range(numCourses)]

    for x, y in prerequisites:
        graph[y].append(x)
        in_degree[x] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count == numCourses


# DFS
def canFinishDFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visitSet = set()

    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
        visitSet.add(crs)

        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(canFinishBFS(5, prerequisites))  # True
print(canFinishDFS(5, prerequisites))  # True
