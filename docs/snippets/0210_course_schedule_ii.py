from collections import defaultdict, deque
from typing import List


# DFS (Neetcode)
def findOrderDFS(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    prereq = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    visit, cycle = set(), set()
    order = []

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if not dfs(pre):
                return False

        cycle.remove(crs)
        visit.add(crs)
        order.append(crs)
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return []

    return order


# BFS - Kahn's Algorithm
def findOrderBFS(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    indegree = [0 for _ in range(numCourses)]

    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    if len(order) == numCourses:
        return order
    else:
        return []


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrderDFS(numCourses, prerequisites))  # [0, 1, 2, 3]
print(findOrderBFS(numCourses, prerequisites))  # [0, 1, 2, 3]
