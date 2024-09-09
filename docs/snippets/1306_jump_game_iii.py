from collections import deque
from typing import List


# BFS
def canReach(arr: List[int], start: int) -> bool:
    n = len(arr)
    visited = [False for _ in range(n)]
    q = deque([start])

    while q:
        i = q.popleft()

        if arr[i] == 0:
            return True

        visited[i] = True

        for j in [i - arr[i], i + arr[i]]:
            if j in range(n) and not visited[j]:
                q.append(j)

    return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(canReach(arr, start))  # True
