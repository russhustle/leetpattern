from collections import deque
from typing import List


# DFS
def canVisitAllRoomsDFS(rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = [False for _ in range(n)]

    def dfs(room):
        visited[room] = True
        for key in rooms[room]:
            if not visited[key]:
                dfs(key)

    dfs(0)

    return all(visited)


# BFS
def canVisitAllRoomsBFS(rooms):
    n = len(rooms)
    visited = [False for _ in range(n)]
    q = deque([0])
    visited[0] = True

    while q:
        room = q.popleft()
        for key in rooms[room]:
            if not visited[key]:
                visited[key] = True
                q.append(key)

    return all(visited)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRoomsDFS(rooms))  # False
print(canVisitAllRoomsBFS(rooms))  # False
