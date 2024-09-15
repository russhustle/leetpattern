from collections import deque
from typing import List


# DP - Kadane
def maxSubarraySumCircularKadane(nums: List[int]) -> int:
    max_sum = min_sum = nums[0]
    max_cur = min_cur = 0
    total = 0

    for num in nums:
        max_cur = max(max_cur + num, num)
        min_cur = min(min_cur + num, num)
        total += num

        max_sum = max(max_sum, max_cur)
        min_sum = min(min_sum, min_cur)

    return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


# Monotonic Queue
def maxSubarraySumCircularMQ(nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * (2 * n + 1)

    for i in range(1, 2 * n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[(i - 1) % n]

    q = deque([0])
    max_sum = float("-inf")

    for i in range(1, 2 * n + 1):
        if q[0] < i - n:
            q.popleft()

        max_sum = max(max_sum, prefix_sum[i] - prefix_sum[q[0]])

        while q and prefix_sum[q[-1]] >= prefix_sum[i]:
            q.pop()

        q.append(i)

    return max_sum


nums = [1, -2, 3, -2]
print(maxSubarraySumCircularKadane(nums))  # 3
print(maxSubarraySumCircularMQ(nums))  # 3
