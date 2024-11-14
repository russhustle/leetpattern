from collections import deque
from typing import List


# Prefix Sum + Monotonic Queue
def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    ps = [0 for _ in range(n + 1)]

    for i in range(n):
        ps[i + 1] = ps[i] + nums[i]

    res = float("inf")
    q = deque()

    for i in range(n + 1):
        while q and ps[i] - ps[q[0]] >= k:
            res = min(res, i - q.popleft())
        while q and ps[i] <= ps[q[-1]]:
            q.pop()
        q.append(i)

    return res if res != float("inf") else -1


nums = [2, -1, 2]
k = 3
print(shortestSubarray(nums, k))  # 3
