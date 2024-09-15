from collections import deque
from typing import List


# Monotonic Queue
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []

    for i, num in enumerate(nums):
        if q and q[0] < i - k + 1:
            q.popleft()

        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # [3, 3, 5, 5, 6, 7]
