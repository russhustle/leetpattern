import bisect
from typing import List


# Prefix Sum
def minSubArrayLenPS(target: int, nums: List[int]) -> int:
    n = len(nums)
    prefix_sums = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

    minLen = float("inf")

    for i in range(n + 1):
        new_target = target + prefix_sums[i]
        bound = bisect.bisect_left(prefix_sums, new_target)
        if bound != len(prefix_sums):
            minLen = min(minLen, bound - i)

    return 0 if minLen == float("inf") else minLen


# Sliding window - Fixed
def minSubArrayLenSW(target: int, nums: List[int]) -> int:
    left, right = 0, 0
    curSum = 0
    minLen = float("inf")

    while right < len(nums):
        curSum += nums[right]

        while curSum >= target:
            minLen = min(minLen, right - left + 1)
            curSum -= nums[left]
            left += 1

        right += 1

    return minLen if minLen != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLenPS(target, nums))  # 2
print(minSubArrayLenSW(target, nums))  # 2
