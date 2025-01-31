from typing import List


# Sliding Window - Fixed
def findMaxAverage(nums: List[int], k: int) -> float:
    cur = sum(nums[:k])
    result = cur

    for i in range(k, len(nums)):
        cur += nums[i] - nums[i - k]
        result = max(result, cur)

    return result / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # 12.75
